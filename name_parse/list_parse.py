# Base
import csv
import random

# Telethon
from telethon_client import get_telethon_client
from telethon.errors import ChatAdminRequiredError
from telethon.tl.functions.channels import GetFullChannelRequest

# Custom functions
from db_functions import get_user_role


async def parse_names_from_group(group_url, user_id) -> None:
    """
    Parse usernames and names of participants from a Telegram group.

    Args:
        group_url (str): URL of the Telegram group.

    Returns:
        None. Writes parsed data to CSV and TXT files.
    """

    try:
        # Establishing a connection with the Telegram client
        client = await get_telethon_client()

        # Retrieving information about the target group
        target_group = await client(GetFullChannelRequest(channel=group_url))

        # Getting all participants of the group
        all_participants = await client.get_participants(target_group.full_chat.id)

        role = await get_user_role(user_id)
        if role == "Базовая":
            num_to_parse = min(130, len(all_participants))
        else:
            num_to_parse = min(200, len(all_participants))

        # Determining the number of users to parse

        users_to_parse = random.sample(all_participants, num_to_parse)

        # Writing usernames and names to a CSV file
        with open("members.csv", "w", encoding="UTF-8") as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(["username", "name", "group"])
            for user in users_to_parse:
                username = user.username if user.username else ""
                first_name = user.first_name if user.first_name else ""
                last_name = user.last_name if user.last_name else ""
                name = (first_name + " " + last_name).strip()
                writer.writerow([username, name, target_group.full_chat])

        # Writing usernames to a TXT file
        with open("members.txt", "w", encoding="UTF-8") as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(["username"])
            for user in users_to_parse:
                if user.username:
                    username = user.username
                    writer.writerow([username])

    except ChatAdminRequiredError:
        return (
            "Для выполнения этой операции требуются административные привилегии чата."
        )

    except Exception as e:
        return f"Произошла ошибка: {e}"

    finally:
        # Disconnecting from the Telegram client
        await client.disconnect()