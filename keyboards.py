# Aiogram
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def parse_names_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🛠 Дополнительно", callback_data="additional")],
            [InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")],
        ]
    )


def payment_menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💰 пополнить баланс", callback_data="topUp")],
            [
                InlineKeyboardButton(
                    text="💎 оформить подписку", callback_data="subscribe"
                )
            ],
            [InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")],
        ]
    )


def menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎮 В главное меню", callback_data="cancel")],
        ]
    )


def cancel_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")],
        ]
    )


def additional_menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎯 фильтр активности", callback_data="activity"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔗 реферальная программа", callback_data="referral"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👨🏻‍💻 написать администратору", url=f"https://t.me/zqwxjs"
                )
            ],
            [InlineKeyboardButton(text="⏪ назад", callback_data="cancel")],
        ]
    )


def topUp_menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💳 Visa, Mastercard, Мир ...", callback_data="cards"
                )
            ],
            [InlineKeyboardButton(text="💵 USDT trc20 / trx", callback_data="USDT")],
            [InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")],
        ]
    )


def cards_menu_keyboard(payment_url, payment_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💸 Оплатить", url=payment_url)],
            [
                InlineKeyboardButton(
                    text="💰 Проверить оплату", callback_data=f"check_pay_{payment_id}"
                )
            ],
            [InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")],
        ]
    )


def payment_result_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👨🏻‍💻 написать администратору", url=f"https://t.me/zqwxjs"
                )
            ],
            [InlineKeyboardButton(text="⏪ назад", callback_data="cancel")],
        ]
    )


def subscribe_menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="▫️ На день 579 ₽", callback_data="subscribe_579"
                )
            ],
            [
                InlineKeyboardButton(
                    text="▫️ На неделю 1550 ₽", callback_data="subscribe_1550"
                )
            ],
            [InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")],
        ]
    )


def activity_answer_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="▫️ Да", callback_data="yes")],
            [InlineKeyboardButton(text="▪️ Нет", callback_data="no")],
            [InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")],
        ]
    )

def ask_parse_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛠 Спарсить по списку", callback_data="parse_list"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Спарсить по сообщениям", callback_data="parse_messages"
                )
            ],
            [InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")],
        ]
    )

def ask_bio_parse_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛠 Спарсить по списку", callback_data="bio_parse_list"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 Спарсить по сообщениям", callback_data="bio_parse_names"
                )
            ],
            [InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")],
        ]
    )

