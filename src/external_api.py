import os
from dotenv import load_dotenv
import requests

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


def convert_to_rub(amount, currency):
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Конвертирует транзакцию из USD или EUR в рубли через обращение к внешнему API для получения
    текущего курса валют.
    """
    if currency == "RUB":
        return amount
    try:
        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/latest",
            params={"symbols": "RUB", "base": currency},
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        rate = data["rates"]["RUB"]
        return amount * rate
    except (requests.exceptions.RequestException, KeyError) as e:
        raise ValueError(f"Произошла ошибка конвертации: {e}")
