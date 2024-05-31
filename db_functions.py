# Async
import asyncpg

# UUID generation for referral links
import uuid

# Date
import datetime
from datetime import datetime, timedelta
import pytz


# function to connect to the database
async def connect_to_db():
    return await asyncpg.connect(
        user="postgres", password="123456", database="parsechat_bot", host="localhost"
    )


# Function to get user balance
async def get_balance(user_id):
    conn = await connect_to_db()
    balance = await conn.fetchval(
        "SELECT balance FROM users WHERE user_id = $1", user_id
    )
    await conn.close()
    return balance


# Function to update user balance
async def update_balance(user_id, amount):
    conn = await connect_to_db()
    async with conn.transaction():
        await conn.execute(
            "INSERT INTO users (user_id, balance) VALUES ($1, $2) "
            "ON CONFLICT (user_id) DO UPDATE SET balance = users.balance + $2",
            user_id,
            amount,
        )
    await conn.close()


# Function to check if a user exists in the database
async def check_user(user_id):
    conn = await connect_to_db()
    user_exists = await conn.fetchval(
        "SELECT EXISTS(SELECT 1 FROM users WHERE user_id = $1)", user_id
    )
    await conn.close()
    return user_exists


# Function to add a user to the database with initial balance
async def add_user(user_id, initial_balance):
    conn = await connect_to_db()
    await conn.execute(
        "INSERT INTO users (user_id, balance) VALUES ($1, $2)", user_id, initial_balance
    )
    await conn.close()


# inserting hash value into database
async def insert_hash(hash_value):
    conn = await connect_to_db()
    await conn.execute("INSERT INTO transactions (hash) VALUES ($1)", hash_value)
    await conn.close()


# checking the presence of a hash in the database
async def check_hash_in_db(hash_value):
    conn = await connect_to_db()
    hash_exists = await conn.fetchval(
        "SELECT EXISTS(SELECT 1 FROM transactions WHERE hash = $1)", hash_value
    )
    await conn.close()
    return hash_exists


# Function to generate a unique referral link for a user
async def generate_referral_link(user_id):
    referral_link = str(uuid.uuid4())[:8]
    conn = await connect_to_db()
    await conn.execute(
        'UPDATE "users" SET referral_link = $1 WHERE user_id = $2',
        referral_link,
        user_id,
    )
    await conn.close()
    return referral_link


async def get_referral_link(user_id):
    conn = await connect_to_db()
    referral_link = await conn.fetchval(
        "SELECT referral_link FROM users WHERE user_id = $1", user_id
    )
    await conn.close()
    return referral_link


# Function to handle referral link click
async def handle_referral_link_click(referral_link, new_user_id):
    conn = await connect_to_db()
    referrer_id = await conn.fetchval(
        "SELECT user_id FROM users WHERE referral_link = $1", referral_link
    )
    if referrer_id:
        await conn.execute(
            "INSERT INTO referrals (referrer_id, referral_id) VALUES ($1, $2)",
            referrer_id,
            new_user_id,
        )
    await conn.close()


async def get_referrer(referral_id):
    conn = await connect_to_db()
    referrer_row = await conn.fetchrow(
        "SELECT referrer_id FROM referrals WHERE referral_id = $1", referral_id
    )
    await conn.close()
    if referrer_row:
        return referrer_row["referrer_id"]
    else:
        return None


async def get_user_role(user_id):
    conn = await connect_to_db()
    row = await conn.fetchrow("SELECT role FROM users WHERE user_id = $1", user_id)
    await conn.close()
    if row:
        if row["role"] is None:
            return "Базовая"
        else:
            return row["role"]
    else:
        return "Базовая"


async def grant_premium_role(user_id, price):
    conn = await connect_to_db()
    
    # Определение времени, на которое продлевается подписка
    if price == 579:
        additional_time = timedelta(days=1)
    else:
        additional_time = timedelta(weeks=1)

    # Получение текущего времени истечения подписки
    result = await conn.fetchrow("SELECT premium_expiration FROM users WHERE user_id = $1", user_id)
    current_expiration = result['premium_expiration']

    # Приведение текущего времени истечения подписки к UTC, если оно не является aware
    if current_expiration and current_expiration.tzinfo is None:
        current_expiration = current_expiration.replace(tzinfo=pytz.utc)

    now_utc = datetime.now(pytz.utc)

    # Если подписка уже существует, добавляем время к текущей дате истечения
    if current_expiration and current_expiration > now_utc:
        expiration_time = current_expiration + additional_time
    else:
        expiration_time = now_utc + additional_time

    expiration_time = expiration_time.replace(tzinfo=None)
    await conn.execute(
        "UPDATE users SET role = $1, premium_expiration = $2 WHERE user_id = $3",
        "premium",
        expiration_time,
        user_id,
    )
    await conn.close()


# Function to remove premium role from a user
async def remove_premium_role(user_id):
    conn = await connect_to_db()
    await conn.execute(
        "UPDATE users SET role = NULL, premium_expiration = NULL WHERE user_id = $1",
        user_id,
    )
    await conn.close()


# Function to check if user has premium role
async def check_premium(user_id):
    conn = await connect_to_db()
    user_row = await conn.fetchrow(
        "SELECT role, premium_expiration FROM users WHERE user_id = $1", user_id
    )
    await conn.close()
    if user_row and user_row["role"] == "premium":
        if user_row["premium_expiration"] > datetime.now(pytz.utc).replace(tzinfo=None):
            return False
        else:
            return True
    return False


# Function to remove premium role if check_premium returns True
async def remove_premium_if_needed(user_id):
    if await check_premium(user_id):
        await remove_premium_role(user_id)
