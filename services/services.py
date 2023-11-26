import requests
from config.config import Config, load_config

config: Config = load_config()

api_key_crypto = config.Rate_bot.api_key_crypto
api_key_currency = config.Rate_bot.api_key_currency


def get_bitcoin_to_usd_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "access_key": api_key_crypto,
        'ids': 'bitcoin',
        'vs_currencies': 'usd',
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200 and 'bitcoin' in data and 'usd' in data['bitcoin']:
            bitcoin_price = data['bitcoin']['usd']
            return bitcoin_price
        else:
           return f"Ошибка: {data}"

    except Exception as e:
        return f"Ошибка при выполнении запроса: {e}"


def get_ethereum_to_usd_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "access_key": api_key_crypto,
        'ids': 'ethereum',
        'vs_currencies': 'usd',
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200 and 'ethereum' in data and 'usd' in data['ethereum']:
            ethereum_price = data['ethereum']['usd']
            return ethereum_price
        else:
            return f"Ошибка: {data}"

    except Exception as e:
        return f"Ошибка при выполнении запроса: {e}"


def get_usd_to_rub_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    params = {
        "app_id": api_key_currency,
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200 and 'rates' in data and 'RUB' in data['rates']:
            usd_to_rub_rate = data['rates']['RUB']
            return usd_to_rub_rate
        else:
            return f"Ошибка: {data}"

    except Exception as e:
        return f"Ошибка при выполнении запроса: {e}"
