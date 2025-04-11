import csv
import os
from typing import Dict, List

import pandas as pd


def read_transactions_csv(file_path: str) -> List[Dict]:
    """Функция для считывания финансовых операций из CSV"""
    file_path = os.path.join("..", "data", "transactions.csv")
    transaction = []
    with open(file_path, encoding="utf-8") as transactions_file:

        reader = csv.DictReader(transactions_file)
        for row in reader:
            transaction.append(row)

    return transaction


def read_transactions_excel(file_path: str) -> List[Dict]:
    """Функция для считывания финансовых операций из Excel"""
    file_path = os.path.join("..", "data", "transactions_excel.xlsx")
    if not os.path.exists(file_path):
        raise FileNotFoundError("Файл не найден!")
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict("records")

        return transactions
    except Exception:
        raise ValueError("Ошибка при чтении файла Excel")
