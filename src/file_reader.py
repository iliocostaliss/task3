from typing import Dict, List

import pandas as pd


def read_transactions_csv(file_path: str) -> List[Dict]:
    """Функция для считывания финансовых операций из CSV"""
    try:
        df = pd.read_csv(file_path, delimiter=";")
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    else:
        df = df.fillna(value="")
        transactions = df.to_dict("records")

    return transactions


def read_transactions_excel(file_path: str) -> List[Dict]:
    """Функция для считывания финансовых операций из Excel"""
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    else:
        df = df.fillna("")
        transactions = df.to_dict("records")
        return transactions
