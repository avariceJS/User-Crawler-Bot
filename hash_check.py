# Base
import requests
import time
import os

# Dotenv
from dotenv import load_dotenv

# Custom functions
from converter import usdt_to_rub
from converter import trx_to_rub
from db_functions import insert_hash
from db_functions import check_hash_in_db

load_dotenv()

# Const
TIME_LIMIT_MINUTES = 20
MY_WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")


async def hash_check(hash):
    """
    Check transaction hash for payment verification.

    Args:
        hash (str): Transaction hash.

    Returns:
        str or tuple: Result message or payment details.
    """

    url = f"https://apilist.tronscanapi.com/api/transaction-info?hash={hash}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            transaction_info = response.json()
            token_transfer_info = transaction_info.get("tokenTransferInfo", {})

            if token_transfer_info:
                tokenType = token_transfer_info.get("tokenType")
                if tokenType == "trc20":
                    if transaction_info.get("confirmed", False):
                        
                        # TRC20 transaction
                        amount = token_transfer_info.get("amount_str", "0")
                        total = int(amount) / 1000000
                        total_amount = await usdt_to_rub(total)
                        total_round = round(total_amount, 0)
                        from_address = token_transfer_info.get("from_address", "")
                        to_address = token_transfer_info.get("to_address", "")
                        timestamp_payment = transaction_info.get("timestamp", "")
                        timestamp_seconds = timestamp_payment / 1000
                        current_time_seconds = time.time()
                        difference_seconds = current_time_seconds - timestamp_seconds
                        difference_minutes = difference_seconds / 60
                        if to_address == MY_WALLET_ADDRESS:
                            if (
                                not await check_hash_in_db(hash)
                                and difference_minutes < TIME_LIMIT_MINUTES
                            ):
                                await insert_hash(hash)
                                return total_round, from_address, to_address
                            else:
                                return "Данный хэш уже использовался или прошло больше 20 минут от времени оплаты."
                        else:
                            return "Хэш из другой транзакции."
                    else:
                        return "Статус оплаты не подтвержден, дождитесь подтверждения оплаты"
                else:

                    # TRX transaction
                    token_transfer_info = transaction_info.get("contractData", {})
                    amount = token_transfer_info.get("amount", 0)
                    from_address = token_transfer_info.get("owner_address", "")
                    to_address = token_transfer_info.get("to_address", "")
            else:

                # TRX transaction
                token_transfer_info = transaction_info.get("contractData", {})
                amount = token_transfer_info.get("amount", 0)
                from_address = token_transfer_info.get("owner_address", "")
                to_address = token_transfer_info.get("to_address", "")

            timestamp_payment = transaction_info.get("timestamp", "")
            total = int(amount) / 1000000
            total_amount = await trx_to_rub(total)
            total_round = round(total_amount, 0)
            timestamp_seconds = timestamp_payment / 1000
            current_time_seconds = time.time()
            difference_seconds = current_time_seconds - timestamp_seconds
            difference_minutes = difference_seconds / 60

            if to_address == MY_WALLET_ADDRESS:
                if (
                    not await check_hash_in_db(hash)
                    and difference_minutes < TIME_LIMIT_MINUTES
                ):
                    await insert_hash(hash)
                    return total_round, from_address, to_address
                else:
                    return "Данный хэш уже использовался или прошло больше 10 минут от времени оплаты."
            else:
                return "Хэш из другой транзакции."
        else:
            return f"Ошибка HTTP {response.status_code}: {response.text}"
    except Exception as e:
        return f"Ошибка при выполнении запроса: {e}"
