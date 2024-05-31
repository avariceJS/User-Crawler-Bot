# Base
import logging
import os

# Dotenv
from dotenv import load_dotenv

# Aiogram
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums import ParseMode
from aiogram import Bot, types
from aiogram.enums import ParseMode
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    BufferedInputFile,
)

# Custom functions
from db_functions import (
    check_user,
    add_user,
    handle_referral_link_click,
    generate_referral_link,
    get_referral_link,
)


# Type
from typing import Union

load_dotenv()

# Initialize the bot with its token
bot = Bot(token=f'{os.getenv("BOT_TOKEN")}', parse_mode=ParseMode.HTML)



# Function to send a document to a specified chat
async def send_document(chat_id, file_name):
    with open(file_name, "rb") as file:
        input_file = BufferedInputFile(file.read(), filename=file_name)
        await bot.send_document(chat_id, input_file)


# Function to edit an existing message
async def edit_message(text, chat_id, message_id, reply_markup=None):
    try:
        logging.info(f"Attempting to edit message {message_id} in chat {chat_id}")
        return await bot.edit_message_text(
            text, chat_id, message_id, reply_markup=reply_markup
        )
    except TelegramBadRequest as e:
        logging.error(f"Failed to edit message {message_id} in chat {chat_id}: {e}")
        return None


async def send_message(target, text, reply_markup=None):
    if hasattr(target, "message") and hasattr(target.message, "chat"):
        chat_id = target.message.chat.id
    elif hasattr(target, "chat"):
        chat_id = target.chat.id
    elif isinstance(target, (int, str)):
        chat_id = target
    else:
        raise ValueError("Invalid target for sending message.")

    message = await bot.send_message(chat_id, text, reply_markup=reply_markup)
    return message


# Function to handle referral link in a message
async def handle_referral_link(message: Message) -> None:
    if len(message.text.split()) > 1:
        parameters = message.text.split()[1]
        if parameters:
            await handle_referral_link_click(parameters, message.from_user.id)


# Function to add a user if they do not already exist in the database
async def add_user_if_not_exists(user_id: int) -> None:
    if not await check_user(user_id):
        await add_user(user_id, initial_balance=15)


# Function to ensure the user has a referral link, generating one if not
async def ensure_referral_link(user_id: int) -> None:
    if not await get_referral_link(user_id):
        await generate_referral_link(user_id)


# Function to send or edit the main menu
async def send_or_edit_main_menu(
    message_or_callback: Union[types.Message, types.CallbackQuery],
    balance: int,
    role: str,
) -> None:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔎 Парсинг", callback_data="parse_names")],
            [
                InlineKeyboardButton(text="💳 Оплата", callback_data="payment"),
                InlineKeyboardButton(text="❓ Помощь", callback_data="help"),
            ],
            [
                InlineKeyboardButton(
                    text="🔬 Спарсить описания профилей", callback_data="bio_parse"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🛸 Спарсить группы/чаты", callback_data="search_groups"
                )
            ],
            [InlineKeyboardButton(text="⏩ Дополнительно", callback_data="additional")],
        ]
    )

    balance_label = f"Баланс: {balance}".ljust(10)
    role_label = f"Роль: {role}".ljust(10)
    if isinstance(message_or_callback, types.Message):
        await message_or_callback.answer(
            f"Главное меню:\n" f"{balance_label} ₽\n" f"{role_label}",
            reply_markup=keyboard,
        )

    elif isinstance(message_or_callback, types.CallbackQuery):
        await edit_message(
            f"Главное меню:\n" f"{balance_label} ₽\n" f"{role_label}",
            message_id=message_or_callback.message.message_id,
            chat_id=message_or_callback.message.chat.id,
            reply_markup=keyboard,
        )
