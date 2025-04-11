import csv
from pathlib import Path
from typing import Dict, List

import pandas as pd


def read_transactions_csv(file_path: Path) -> List[Dict]:
    """Функция для считывания финансовых операций из CSV"""
    path = Path(file_path).resolve()
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    transactions = []
    with open(file_path, encoding="utf-8") as transactions_file:
        reader = csv.DictReader(transactions_file)
        for row in reader:
            transactions.append(row)
    return transactions


def read_transactions_excel(file_path: Path) -> List[Dict]:
    """Функция для считывания финансовых операций из Excel"""
    file_path = Path(file_path).resolve()
    if not file_path.exists():
        raise FileNotFoundError("Файл не найден!")
    try:
        df = pd.read_excel(file_path)
        return df.to_dict("records")
    except Exception:
        raise ValueError("Ошибка при чтении файла Excel")
