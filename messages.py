# Custom keyboards functions
from keyboards import (
    ask_parse_keyboard,
    ask_bio_parse_keyboard,
    parse_names_keyboard,
    payment_menu_keyboard,
    menu_keyboard,
    cancel_keyboard,
    additional_menu_keyboard,
    topUp_menu_keyboard,
    cards_menu_keyboard,
    subscribe_menu_keyboard,
    activity_answer_keyboard,
)

# Custom functions
from bot_utils import edit_message, send_message


async def send_parse_names_message(callback):
    return await edit_message(
        "Отправьте ссылку на открытую группу, откуда нужно собрать пользователей(пользователи с базовой ролью получают только 70% от всех пользователей)",
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=parse_names_keyboard(),
    )


async def send_parsing_process_message(callback):
    return await send_message(callback.from_user.id, "⏳ идет процесс парсинга....")


async def send_invalid_url_message(message):
    return await send_message(
        message,
        "Пожалуйста, введите корректную ссылку на группу или чат.",
        reply_markup=cancel_keyboard(),
    )


async def send_ask_bio_parse_message(message):
    return await send_message(
        message,
        "если группы с закрытым списком участников выберите способ по сообщениям \n \nВыберите как спарсить пользователей:",
        reply_markup=ask_bio_parse_keyboard(),
    )


async def send_ask_parse_message(message):
    return await send_message(
        message,
        "если группы с закрытым списком участников выберите способ по сообщениям \n \nВыберите как спарсить пользователей:",
        reply_markup=ask_parse_keyboard(),
    )


async def send_topUp_confirmation(callback):
    await send_message(
        callback,
        " Выберите способ оплаты",
        reply_markup=topUp_menu_keyboard(),
    )


async def send_successful_parse_message(callback):
    await send_message(
        callback,
        "Парсинг завершен успешно",
        reply_markup=menu_keyboard(),
    )


async def send_file_filtering_error_message(callback):
    return await send_message(
        callback,
        "Произошла ошибка при фильтрации файла",
        reply_markup=menu_keyboard(),
    )


async def send_file_successfully_filtered_message(callback):
    return await send_message(
        callback,
        "файл успешно отфильтрован",
        reply_markup=menu_keyboard(),
    )


async def send_subscribe_confirmation(callback, price, user_balance, remaining_balance):
    await edit_message(
        f"Подписка стоит {price} ₽. \n Ваш баланс: {user_balance} ₽. \n Для оформления подписки нужно будет доплатить {remaining_balance} ₽.  \n \n Выберите способ оплаты",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=topUp_menu_keyboard(),
    )


async def send_successful_payment_message(callback):
    await edit_message(
        "Оплата прошла успешно!",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=menu_keyboard(),
    )


async def send_additional_menu_message(callback, balance, role):
    await edit_message(
        f"Главное меню: \n Баланс: {balance} ₽\n Роль: {role}",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=additional_menu_keyboard(),
    )


async def send_usdt_menu_message(callback, usdt, trx):
    return await edit_message(
        f" Сумма оплаты: {usdt} usdt / {trx} trx \n Адрес для перевода: \n TKFyKaEDWEzorUzHNaTFEW9cpTPqacc1PM \n \n После оплаты отправьте сюда хэш транзакции в течение 20 минут",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=cancel_keyboard(),
    )


async def send_cards_menu_message(callback, payment_url, payment_id):
    await edit_message(
        f"Для пополнения баланса перейдите по ссылке: {payment_url} \n \n Чтобы деньги поступили на счет, после перевода нажмите на кнопку Проверить оплату.\n Если вы пополнили счет, но деньги на балансе не появились - напишите администратору",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=cards_menu_keyboard(payment_url, payment_id),
    )


async def send_subscribe_menu_message(callback):
    await edit_message(
        "Выберите вариант подписки",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=subscribe_menu_keyboard(),
    )


async def send_referral_menu_message(callback, referral_link):
    await edit_message(
        f"🔗 Вы будете получать на баланс 20% от пополнений всех пользователей, зашедших в бот по вашей ссылке! Реферальная ссылка: https://t.me/parsechat_bot?start={referral_link}",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=menu_keyboard(),
    )


async def send_activity_menu_message(callback):
    return await edit_message(
        "С помощью этой функции вы можете отфильтровать пользователей по дате их захода в сеть. Отправьте таблицу, которую бот выдал вам в результате парсинга",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=cancel_keyboard(),
    )


async def send_activity_process_message(callback):
    await edit_message(
        'Добавлять в результаты людей, которые были "недавно" ?',
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=activity_answer_keyboard(),
    )


async def send_topUp_message(callback):
    await edit_message(
        "Отправьте сумму для пополнения баланса (₽)",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=cancel_keyboard(),
    )


async def send_bio_parse_message(callback):
    return await edit_message(
        "Отправьте ссылку на группу, откуда нужно собрать информацию о пользователях. \n \n пользователи с базовой ролью получают только 70% от всех пользователей",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=cancel_keyboard(),
    )


async def send_search_groups_message(callback):
    return await edit_message(
        "Отправьте ключевые слова / фразы для поиска (не больше 20 в бесплатном режиме) \n \n"
        "Слова должны быть разделены запятой!",
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=cancel_keyboard(),
    )


async def send_payment_menu_message(callback):
    await edit_message(
        "🌟 <b>Подписка Премиум</b> 🌟\n\n"
        "🚀 <b>Быстрейший парсинг:</b> Ваши запросы и парсинг будут обрабатываться быстрее.\n"
        "📈 <b>Больше пользователей:</b> Парсер охватывает большее количество пользователей Telegram.\n"
        "🔍 <b>Подробная информация:</b> Сбор большей информации о пользователях.\n"
        "👥 <b>Расширенные возможности:</b> Парсинг большего числа групп и чатов.\n"
        "🔐 <b>Подпишитесь сейчас и получите максимум возможностей!</b>",
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=payment_menu_keyboard(),
    )


async def send_help_menu_message(callback):
    await edit_message(
        "🤖 <b>Добро пожаловать в раздел помощи нашего бота!</b>\n\n"
        "Здесь вы найдете информацию о функциях и возможностях нашего бота.\n\n"
        "📋 <b>Основные функции:</b>\n"
        "<b>1. Парсинг никнеймов</b>\n"
        "   - 📂 Сбор никнеймов участников групп и чатов.\n"
        '   - <b>Использование:</b> перейдите в <i>"Парсинг"</i> и укажите ссылку на чат/группу.\n\n'
        "<b>2. Пополнение баланса</b>\n"
        "   - 💳 Для использования платных функций.\n"
        '   - <b>Использование:</b> перейдите в <i>"Оплата"</i> и следуйте инструкциям.\n\n'
        "<b>3. Оплата подписки</b>\n"
        "   - 🌟 Доступ к премиум-функциям.\n"
        '   - <b>Использование:</b> перейдите в <i>"Оплата"</i> и следуйте инструкциям.\n\n'
        "<b>4. Парсинг описания профилей</b>\n"
        "   - 📝 Сбор описаний профилей участников.\n"
        '   - <b>Использование:</b> перейдите в <i>"Спарсить описание профилей"</i> и укажите ссылку.\n\n'
        "<b>5. Поиск групп и чатов по ключевым словам</b>\n"
        "   - 🔍 Поиск групп и чатов по ключевым словам.\n"
        '   - <b>Использование:</b> перейдите в <i>"Спарсить группы/чаты"</i> и укажите ключевые слова.\n\n'
        "<b>6. Фильтрация пользователей по дате активности</b>\n"
        "   - 📅 Фильтрация по последней активности.\n"
        '   - <b>Использование:</b> в <i>"Дополнительно"</i> выберите <i>"Фильтр активности"</i> и следуйте инструкциям.\n\n'
        "<b>7. Реферальная программа</b>\n"
        "   - 🎁 Приглашайте друзей и получайте бонусы.\n"
        '   - <b>Использование:</b> в <i>"Дополнительно"</i> выберите <i>"Реферальная программа"</i> для получения реферальной ссылки.\n\n'
        "👨‍💻 Разработчик - @zqwxjs",
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=menu_keyboard(),
    )
