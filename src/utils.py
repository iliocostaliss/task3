import json
import logging
import os


logger = logging.getLogger("utils")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "..\\logs\\", "utils.log"), "w", "utf-8"
)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def dict_transactions(file_path):
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        logger.info("Выполняем запрос")
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

            if isinstance(data, list):
                return data
            else:
                logger.info("Транзакции не найдены")
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден")
        return []


transactions = dict_transactions("..\\data\\operations.json")
print(transactions)

