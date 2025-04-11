import csv
import os

import pandas as pd


def read_transactions_csv(file_path):
    """Функция для считывания финансовых операций из CSV"""
    file_path = os.path.join("..", "data", "transactions.csv")
    transaction = []
    with open(file_path, encoding="utf-8") as transactions_file:

        reader = csv.DictReader(transactions_file)
        for row in reader:
            transaction.append(row)

    return transaction


transactions = read_transactions_csv("transactions.csv")
for transaction in transactions:
    print(transaction)


def read_transactions_excel(file_path):
    """Функция для считывания финансовых операций из Excel"""
    try:
        file_path = os.path.join("..", "data", "transactions_excel.xlsx")
        df = pd.read_excel(file_path)
        transactions = df.to_dict("records")

        return transactions
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден!")


transactions = read_transactions_excel("transactions_excel.xlsx")
print(transactions)
