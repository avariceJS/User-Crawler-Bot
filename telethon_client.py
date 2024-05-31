# Base
import os

# Dotenv
from dotenv import load_dotenv

# Telethon
from telethon import TelegramClient


async def get_telethon_client():
    """
    Establishes a connection with the Telegram client.

    Returns:
        TelegramClient: A connected instance of the Telegram client.
    """

    load_dotenv()

    # Telegram API credentials and phone number
    api_id = os.getenv("API_ID")
    api_hash = os.getenv("API_HASH")
    phone = os.getenv("PHONE")

    # Connecting to the Telegram client
    client = TelegramClient(phone, api_id, api_hash)
    await client.connect()

    # Authenticating the user if not authorized
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        await client.sign_in(phone, input("Enter a code:"))

    return client
