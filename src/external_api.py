import json
import os

import requests
from dotenv import load_dotenv

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
            "https://api.apilayer.com/exchangerates_data/convert",
            params={"to": "RUB", "from": currency, "amount": amount},
            headers=headers,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        if "result" not in data:
            raise ValueError("Некорректный ответ API: отсутствует поле 'result'")

        return data["result"]

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Ошибка запроса к API: {str(e)}")
    except KeyError as e:
        raise ValueError(f"Некорректный формат ответа API: {str(e)}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка обработки ответа API: {str(e)}")
