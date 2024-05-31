# Base
import os

# Dotenv
from dotenv import load_dotenv

# YooKassa
import yookassa
from yookassa import Payment
import uuid

load_dotenv()

# Configuring YooKassa account details
yookassa.Configuration.account_id = os.getenv("ACCOUNT_ID")
yookassa.Configuration.secret_key = os.getenv("SECRET_KEY")


def create(amount, chat_id):
    """
    Create a payment request.

    Args:
        amount (float): The amount to be paid.
        chat_id (int): ID of the chat associated with the payment.

    Returns:
        tuple: A tuple containing the payment confirmation URL and ID.
    """

    # Generating a unique ID for the payment
    id_key = str(uuid.uuid4())

    # Creating the payment request
    payment = Payment.create(
        {
            "amount": {"value": amount, "currency": "RUB"},
            "payment_method_data": {"type": "bank_card"},
            "confirmation": {
                "type": "redirect",
                "return_url": "https://t.me/parsechat_bot",
            },
            "capture": True,
            "metadata": {"chat_id": chat_id},
            "description": {"Пополнение баланса"},
        },
        id_key,
    )

    return payment.confirmation.confirmation_url, payment.id


async def check(payment_id):
    """
    Check the status of a payment.

    Args:
        payment_id (str): ID of the payment to be checked.

    Returns:
        dict or bool: Metadata associated with the payment if successful, False otherwise.
    """

    payment = yookassa.Payment.find_one(payment_id)
    if payment.status == "succeeded":
        return payment.metadata
    else:
        return False
