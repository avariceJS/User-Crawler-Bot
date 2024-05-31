# HTML parsing
from bs4 import BeautifulSoup

# Async
import aiohttp

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


async def rub_to_usdt(amount):
    """
    Converts a given amount of RUB to USDT using exchange rates from Google.

    Args:
        amount (float): The amount of RUB to convert.

    Returns:
        float: The converted amount in USDT.
    """

    url = f"https://www.google.com/search?q={amount}+rub+to+usdt+exchange+rates"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()
    soup = BeautifulSoup(html, "html.parser")
    exchange_rate_div = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
    exchange_rate_text = exchange_rate_div.text.strip()
    exchange_rate_text = exchange_rate_text.replace(".", "").replace(",", ".")
    exchange_rate = float(exchange_rate_text.split()[0])
    total = round(exchange_rate, 1)
    return total


async def rub_to_trx(amount):
    """
    Converts a given amount of RUB to TRX using exchange rates from Google.

    Args:
        amount (float): The amount of RUB to convert.

    Returns:
        float: The converted amount in TRX.
    """

    url = f"https://www.google.com/search?q={amount}+rub+to+trx+exchange+rates"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()
    soup = BeautifulSoup(html, "html.parser")
    exchange_rate_div = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
    exchange_rate_text = exchange_rate_div.text.strip()
    exchange_rate_text = exchange_rate_text.replace(".", "").replace(",", ".")
    exchange_rate = float(exchange_rate_text.split()[0])
    total = round(exchange_rate, 1)
    return total


async def usdt_to_rub(amount):
    """
    Converts a given amount of USDT to RUB using exchange rates from Google.

    Args:
        amount (float): The amount of USDT to convert.

    Returns:
        float: The converted amount in RUB.
    """

    url = f"https://www.google.com/search?q={amount}+usdt+to+rub+exchange+rates"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()
    soup = BeautifulSoup(html, "html.parser")
    exchange_rate_div = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
    exchange_rate_text = exchange_rate_div.text.strip()
    exchange_rate_text = exchange_rate_text.replace(".", "").replace(",", ".")
    exchange_rate = float(exchange_rate_text.split()[0])
    return exchange_rate


async def trx_to_rub(amount):
    """
    Converts a given amount of TRX to RUB using exchange rates from Google.

    Args:
        amount (float): The amount of TRX to convert.

    Returns:
        float: The converted amount in RUB.
    """

    url = f"https://www.google.com/search?q={amount}+trx+to+rub+exchange+rates"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()
    soup = BeautifulSoup(html, "html.parser")
    exchange_rate_div = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
    exchange_rate_text = exchange_rate_div.text.strip()
    exchange_rate_text = exchange_rate_text.replace(".", "").replace(",", ".")
    exchange_rate = float(exchange_rate_text.split()[0])
    return exchange_rate
