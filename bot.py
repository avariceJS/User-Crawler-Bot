# Base
import asyncio
import logging
import sys
import re
import os

# Dotenv
from dotenv import load_dotenv

# Custom functions
from bio_parse.list_parse import bio_parse_from_group
from bio_parse.chat_parse import bio_parse_group_chat
from telegram_scraper import fetch_telegram_data
from converter import rub_to_usdt
from hash_check import hash_check
from payment_functions import create, check
from converter import rub_to_trx
from name_parse.list_parse import parse_names_from_group
from filter import filter_users
from name_parse.chat_parse import fetch_chat_users
from bot_utils import (
    send_document,
    handle_referral_link,
    add_user_if_not_exists,
    ensure_referral_link,
    send_or_edit_main_menu,
)

# Custom db functions
from db_functions import (
    grant_premium_role,
    get_user_role,
    remove_premium_if_needed,
    update_balance,
    get_referrer,
    get_balance,
    get_referral_link,
)

# Aiogram
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    BufferedInputFile,
)

# Custom keyboards functions
from keyboards import (
    cancel_keyboard,
    payment_result_keyboard,
)

# Custom messages functions
from messages import (
    send_file_successfully_filtered_message,
    send_file_filtering_error_message,
    send_ask_parse_message,
    send_ask_bio_parse_message,
    send_invalid_url_message,
    send_payment_menu_message,
    send_help_menu_message,
    send_parsing_process_message,
    send_bio_parse_message,
    send_search_groups_message,
    send_successful_parse_message,
    send_additional_menu_message,
    send_activity_menu_message,
    send_activity_process_message,
    send_cards_menu_message,
    send_parse_names_message,
    send_referral_menu_message,
    send_subscribe_menu_message,
    send_subscribe_confirmation,
    send_successful_payment_message,
    send_topUp_message,
    send_topUp_confirmation,
    send_usdt_menu_message,
)

load_dotenv()

# Initialize the bot with its token
bot = Bot(token=f'{os.getenv("BOT_TOKEN")}')

# Include the Router into the Dispatcher
form_router = Router()
dp = Dispatcher()
dp.include_router(form_router)

GROUP_CHAT_URL_PATTERN = re.compile(
    r"^(https?:\/\/)?(www\.)?(t\.me\/|telegram\.me\/|t\.me\/joinchat\/|telegram\.me\/joinchat\/)[a-zA-Z0-9_\/]+$"
)


# States
class Form(StatesGroup):
    parse_names_state = State()
    bio_parse_state = State()
    search_groups_state = State()
    top_up_state = State()
    activity_state = State()
    hash_check_state = State()


@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    await remove_premium_if_needed(user_id)
    await handle_referral_link(message)
    await add_user_if_not_exists(user_id)
    await ensure_referral_link(user_id)
    balance = await get_balance(user_id)
    role = await get_user_role(user_id)
    await send_or_edit_main_menu(message, balance, role)


@form_router.callback_query(lambda c: c.data == "parse_names")
async def handle_parse_names_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.parse_names_state)
    parse_url_message = await send_parse_names_message(callback)
    await state.update_data(parse_url_message_id=parse_url_message.message_id)

    @form_router.message(Form.parse_names_state)
    async def handle_parse_names_url(message: Message, state: FSMContext) -> None:
        group_url = message.text
        if not GROUP_CHAT_URL_PATTERN.match(group_url):
            invalid_url = await send_invalid_url_message(callback)
            await state.update_data(invalid_url_message_id=invalid_url.message_id)
            return
        await state.update_data(group_url=group_url)
        ask_parse_message = await send_ask_parse_message(message)
        await state.update_data(ask_parse_message_id=ask_parse_message.message_id)


@form_router.callback_query(lambda c: c.data in ["parse_list", "parse_messages"])
async def handle_parse_choice_callback(
    callback: types.CallbackQuery, state: FSMContext
):
    user_id = callback.from_user.id
    choice = callback.data
    limit = 500 if await get_user_role(callback.from_user.id) == "Базовая" else 797
    data = await state.get_data()
    group_url = data.get("group_url")
    wait_message = await send_parsing_process_message(callback)

    if choice == "parse_list":
        await parse_names_from_group(group_url, user_id)
    elif choice == "parse_messages":
        await fetch_chat_users(group_url, limit, user_id)

    await send_document(callback.message.chat.id, "members.txt")
    await send_document(callback.message.chat.id, "members.csv")
    data = await state.get_data()
    parse_url_message_id = data.get("parse_url_message_id")
    ask_parse_message_id = data.get("ask_parse_message_id")
    invalid_url_message_id = data.get("invalid_url_message_id")
    await send_successful_parse_message(callback)
    if invalid_url_message_id:
        await bot.delete_message(callback.message.chat.id, invalid_url_message_id)
    await bot.delete_message(callback.message.chat.id, parse_url_message_id)
    await bot.delete_message(callback.message.chat.id, ask_parse_message_id)
    await bot.delete_message(callback.message.chat.id, wait_message.message_id)


@form_router.callback_query(lambda c: c.data == "payment")
async def handle_payment_menu_callback(callback: types.CallbackQuery):
    await send_payment_menu_message(callback)


@form_router.callback_query(lambda c: c.data == "help")
async def handle_help_callback(callback: types.CallbackQuery):
    await send_help_menu_message(callback)


@form_router.callback_query(lambda c: c.data == "bio_parse")
async def handle_bio_parse_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.bio_parse_state)
    bio_parse_message = await send_bio_parse_message(callback)
    await state.update_data(bio_parse_message_id=bio_parse_message.message_id)

    @form_router.message(Form.bio_parse_state)
    async def handle_bio_parse_url(message: Message, state: FSMContext) -> None:
        url_group = message.text
        if not GROUP_CHAT_URL_PATTERN.match(url_group):
            keyboard = cancel_keyboard()
            await message.answer(
                "Пожалуйста, введите корректную ссылку на группу или чат.",
                reply_markup=keyboard,
            )
            return
        await state.update_data(url_group=url_group)
        ask_bio_parse_message = await send_ask_bio_parse_message(message)
        await state.update_data(
            ask_bio_parse_message_id=ask_bio_parse_message.message_id
        )


@form_router.callback_query(lambda c: c.data in ["bio_parse_list", "bio_parse_names"])
async def handle_bio_parse_choice_callback(
    callback: types.CallbackQuery, state: FSMContext
):
    user_id = callback.from_user.id
    choice = callback.data
    limit = 410 if await get_user_role(callback.from_user.id) == "Базовая" else 599
    data = await state.get_data()
    group_url = data.get("url_group")
    wait_message = await send_parsing_process_message(callback)

    if choice == "bio_parse_names":
        await bio_parse_group_chat(group_url, limit, user_id)
    elif choice == "bio_parse_list":
        await bio_parse_from_group(group_url, callback.from_user.id)

    data = await state.get_data()
    bio_parse_message_id = data.get("bio_parse_message_id")
    ask_bio_parse_message_id = data.get("ask_bio_parse_message_id")
    await bot.delete_message(callback.message.chat.id, ask_bio_parse_message_id)
    await bot.delete_message(callback.message.chat.id, bio_parse_message_id)
    await bot.delete_message(callback.message.chat.id, wait_message.message_id)
    await send_document(callback.message.chat.id, "user_info.xlsx")
    await send_successful_parse_message(callback)


@form_router.callback_query(lambda c: c.data == "search_groups")
async def handle_search_groups_callback(
    callback: types.CallbackQuery, state: FSMContext
):
    await state.set_state(Form.search_groups_state)
    search_groups_message = await send_search_groups_message(callback)
    await state.update_data(search_groups_message_id=search_groups_message.message_id)

    @form_router.message(Form.search_groups_state)
    async def handle_search_groups_keyword(message: Message, state: FSMContext) -> None:
        user_id = message.from_user.id
        keyword = message.text
        word_limit = 20
        word_count = len(keyword.split())

        if word_count > word_limit:
            await message.answer(
                "Извините, пользователи с базовой ролью могут отправлять не более 20 слов."
            )
            return

        wait_message = await send_parsing_process_message(callback)
        await fetch_telegram_data(user_id, keyword)
        await send_document(callback.message.chat.id, "group_chat_data.xlsx")
        data = await state.get_data()
        search_groups_message_id = data.get("search_groups_message_id")
        await bot.delete_message(callback.message.chat.id, search_groups_message_id)
        await bot.delete_message(callback.message.chat.id, wait_message.message_id)
        await send_successful_parse_message(callback)


@form_router.callback_query(lambda c: c.data == "additional")
async def handle_additional_menu_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    role = await get_user_role(user_id)
    balance = await get_balance(user_id)
    await send_additional_menu_message(callback, balance, role)


@form_router.callback_query(lambda c: c.data == "cancel")
async def handle_cancel_menu_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    role = await get_user_role(user_id)
    balance = await get_balance(user_id)
    await send_or_edit_main_menu(callback, balance, role)


@form_router.callback_query(lambda c: c.data == "referral")
async def handle_referral_menu_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    referral_link = await get_referral_link(user_id)
    if referral_link:
        await send_referral_menu_message(callback, referral_link)
    else:
        await bot.answer_callback_query(
            callback.id, "Ошибка при получении реферальной ссылки."
        )


@form_router.callback_query(lambda c: c.data == "activity")
async def handle_activity_menu_callback(
    callback: types.CallbackQuery, state: FSMContext
):
    await state.set_state(Form.activity_state)
    activity_menu_message = await send_activity_menu_message(callback)
    await state.update_data(activity_menu_message_id=activity_menu_message.message_id)

    @form_router.message(Form.activity_state)
    async def handle_activity_file(message: types.Message):
        if message.document is None:
            keyboard = cancel_keyboard()
            await message.answer(
                "Пожалуйста, отправьте excel файл.", reply_markup=keyboard
            )
            return
        if (
            message.document.mime_type
            != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ):
            await message.answer("Пожалуйста, отправьте файл в формате .xlsx")
            return

        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path

        await bot.download_file(file_path, file_path.split("/")[-1])

        keep_recently_active = True
        filtered_file_path = filter_users(
            file_path.split("/")[-1], keep_recently_active
        )
        data = await state.get_data()
        activity_menu_message_id = data.get("activity_menu_message_id")
        if filtered_file_path:
            with open(filtered_file_path, "rb") as file:
                input_file = BufferedInputFile(
                    file.read(), filename="activity_filtered.xlsx"
                )
                await bot.delete_message(
                    callback.message.chat.id, activity_menu_message_id
                )
                await bot.send_document(message.chat.id, input_file)
                await send_file_successfully_filtered_message(callback)
        else:
            await bot.delete_message(callback.message.chat.id, activity_menu_message_id)
            await send_file_filtering_error_message(callback)

    @form_router.callback_query(lambda c: c.data == "activity")
    async def handle_activity_callback(callback: types.CallbackQuery):
        await send_activity_process_message(callback)


@form_router.callback_query(lambda c: c.data == "topUp")
async def handle_topUp_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.top_up_state)
    await send_topUp_message(callback)

    @form_router.message(Form.top_up_state)
    async def handle_topUp_amount(message: Message, state: FSMContext) -> None:
        keyboard = cancel_keyboard()
        try:
            topup_amount = float(message.text)
        except ValueError:
            await message.answer(
                "Некорректная сумма. Пожалуйста, введите число", reply_markup=keyboard
            )
            return

        if topup_amount <= 0:
            await message.answer("Сумма должна быть больше нуля.")
            return

        await state.update_data(topup_amount=topup_amount)
        await send_topUp_confirmation(callback)


@form_router.callback_query(lambda c: c.data == "cards")
async def handle_cards_callback(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    remaining_balance = data.get("remaining_balance")
    if remaining_balance:
        payment_url, payment_id = create(remaining_balance, callback.message.chat.id)
    else:
        deposit = data.get("topup_amount", "")
        payment_url, payment_id = create(deposit, callback.message.chat.id)
    await send_cards_menu_message(callback, payment_url, payment_id)


@form_router.callback_query(lambda c: c.data == "USDT")
async def handle_usdt_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.hash_check_state)
    data = await state.get_data()
    remaining_balance = data.get("remaining_balance")
    if remaining_balance:
        usdt = await rub_to_usdt(remaining_balance)
        trx = await rub_to_trx(remaining_balance)
    else:
        deposit = data.get("topup_amount", "")
        usdt = await rub_to_usdt(deposit)
        trx = await rub_to_trx(deposit)

    await send_usdt_menu_message(callback, usdt, trx)

    @form_router.message(Form.hash_check_state)
    async def handle_usdt_payment_result(message: Message, state: FSMContext) -> None:
        hash = message.text
        result = await hash_check(hash)
        if isinstance(result, tuple):
            amount, owner_address, to_address = result
            await message.answer(f"Статус оплаты: Подтверждено")
            await message.answer(f"Сумма: {amount}")
            await message.answer(f"Адрес отправителя: {owner_address}")
            await message.answer(f"Адрес получателя: {to_address}")
            user_id = callback.from_user.id
            await update_balance(user_id, amount)
            referrer = await get_referrer(user_id)
            if referrer:
                income = amount * 0.2
                round_income = round(income, 0)
                await update_balance(referrer, round_income)
        else:
            keyboard = payment_result_keyboard()
            await message.answer(
                f"Ошибка при проверке hash: \n {result}. Пожалуйста, попробуйте еще раз. \n Вы можете отслеживать статус транзакции тут: \n https://tronscan.org/#/transaction/. \n \n Если транзакция подтверждена в сети, но бот так и не зачислил деньги на баланс, пожалуйста, напишите администратору",
                reply_markup=keyboard,
                disable_web_page_preview=True,
            )


@form_router.callback_query(lambda c: "check_pay" in c.data)
async def handle_check_payment_callback(
    callback: types.CallbackQuery, state: FSMContext
):
    result = await check(callback.data.split("_")[-1])
    if result:
        data = await state.get_data()
        amount = data.get("topup_amount", "")
        user_id = callback.from_user.id
        await update_balance(user_id, amount)
        referrer = await get_referrer(user_id)
        if referrer:
            income = amount * 0.2
            round_income = round(income, 0)
            await update_balance(referrer, round_income)
        await callback.message.answer("Оплата прошла успешно")
    else:
        await callback.message.answer("Оплата еще не прошла или возникла ошибка")


@form_router.callback_query(lambda c: c.data == "subscribe")
async def handle_subscribe_callback(callback: types.CallbackQuery):
    await send_subscribe_menu_message(callback)


@form_router.callback_query(lambda c: c.data.startswith("subscribe_"))
async def handle_subscribe_payment(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    user_balance = await get_balance(user_id)
    price = int(callback.data.split("_")[1])

    if user_balance >= price:
        await update_balance(user_id, -price)
        await grant_premium_role(user_id, price)
        await send_successful_payment_message(callback)
    else:
        remaining_balance = price - user_balance
        await state.update_data(remaining_balance=remaining_balance)
        await send_subscribe_confirmation(
            callback, price, user_balance, remaining_balance
        )


# Main function to start the bot
async def main():
    await dp.start_polling(bot)


# Entry point
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
