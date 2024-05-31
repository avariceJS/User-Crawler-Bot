# Telethon
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerUser

# Async
import asyncio
import aiohttp

# Custom functions
from telethon_client import get_telethon_client
from db_functions import get_user_role


async def members_id(group_link, limit, user_id):
    """
    Retrieve user IDs from a chat.

    Args:
        group_link (str): The link to the Telegram group.
        limit (int): The limit on the number of messages to analyze.

    Returns:
        set: A set of unique user IDs.
    """

    role = await get_user_role(user_id)
    async def delay():
        if role == "premium":
            await asyncio.sleep(23)
        else:
            await asyncio.sleep(33)

    client = await get_telethon_client()
    entity = await client.get_entity(group_link)
    usernames = set()
    message_count = 0
    has_more_messages = True
    last_message_id = 0

    while has_more_messages and message_count < limit:

        # Request message history
        messages = await client(
            GetHistoryRequest(
                peer=entity,
                limit=100,
                offset_date=None,
                offset_id=last_message_id,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0,
            )
        )

        for message in messages.messages:
            if isinstance(message.from_id, PeerUser):
                user_id = message.from_id.user_id
                usernames.add(user_id)
                message_count += 1
                if message_count >= limit:
                    break

                # Pause to prevent request rate limits
                if message_count % 399 == 0:
                    await delay()

        if messages.messages:
            last_message_id = messages.messages[-1].id
        has_more_messages = len(messages.messages) > 0

    await client.disconnect()

    return usernames


async def fetch_description(client, user_id):
    """
    Retrieve a user's description by their ID.

    Args:
        client (TelegramClient): The Telethon client.
        user_id (int): The user's ID.

    Returns:
        str or None: The username or None if not available.
    """

    try:
        user = await client.get_entity(user_id)
        username = user.username
        if username:
            return username
        else:
            return None

    except Exception as e:
        return None


async def bio_parse(user_ids):
    """
    Parse user biographies.

    Args:
        user_ids (set): A set of user IDs.

    Returns:
        list: A list of user descriptions.
    """
        
    client = await get_telethon_client()  # await the function call
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_description(client, user_id) for user_id in user_ids]
        descriptions = await asyncio.gather(*tasks)
        await client.disconnect()
        return descriptions


async def write_usernames_to_files(usernames):
    """
     Write user names in files.

     Args:
         usernames (SET): many user names.
    """
    
    with open("members.txt", "w") as txt_file:
        for username in usernames:
            txt_file.write(f"{username}\n")

    with open("members.csv", "w") as csv_file:
        csv_file.write("username:\n \n")
        for username in usernames:
            csv_file.write(f"{username}\n")


async def fetch_chat_users(group_link, limit, user_id):
    """
     The main function for obtaining and recording the names of chat users.

     Args:
         Group_Link (str): link to the group in Telegram.
         Limit (int): restriction on the number of messages for analysis.
    """
    
    user_ids = await members_id(group_link, limit, user_id)
    descriptions = await bio_parse(user_ids)
    usernames = set(descriptions) - {None}
    await write_usernames_to_files(usernames)
