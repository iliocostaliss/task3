import os

from src.file_reader import read_transactions_csv, read_transactions_excel
from src.processing import filter_by_state, sort_by_date
from src.transaction_utils import filter_operations_by_description
from src.utils import dict_transactions
from src.widget import get_date, mask_account_card


def display_transaction(transaction: dict) -> None:
    """Выводит транзакции на экран."""
    try:
        date = get_date(transaction.get("date", ""))
        description = transaction.get("description", "Нет описания")
        from_info = mask_account_card(transaction["from"]) if transaction.get("from") else ""
        to_info = mask_account_card(transaction["to"])

        amount = float(transaction.get("amount", 0))
        currency = transaction.get("currency_name", "RUB")

        output = f"""
    {date} {description}
    {f"{from_info} -> " if from_info else ""}{to_info}
    Сумма: {round(amount, 2)} {currency}
        """
        print(output.strip())
        print("")

    except Exception as e:
        print(f"Ошибка при выводе транзакции: {e}")


def convert_transaction(transaction_list: list[dict]) -> list[dict]:
    result = []
    for tr in transaction_list:
        tr_temp = {
            "id": tr.get("id", ""),
            "state": tr.get("state", ""),
            "date": tr.get("date", ""),
            "amount": tr.get("operationAmount", {}).get("amount", ""),
            "currency_name": tr.get("operationAmount", {}).get("currency", {}).get("name", ""),
            "currency_code": tr.get("operationAmount", {}).get("currency", {}).get("code", ""),
            "from": tr.get("from", ""),
            "to": tr.get("to", ""),
            "description": tr.get("description", ""),
        }
        result.append(tr_temp)
    return result


def get_file_reader(file_type: str):
    """Возвращает функцию для чтения файла в зависимости от типа."""
    readers = {
        "1": dict_transactions,
        "2": read_transactions_csv,
        "3": read_transactions_excel,
    }
    return readers.get(file_type)


def main():
    try:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        file_type = input("Выберите необходимый пункт меню: ").strip()
        reader = get_file_reader(file_type)
        if not reader:
            print("Неверный выбор файла. Программа завершена.")
            return

        file_name = (
            "operations.json"
            if file_type == "1"
            else "transactions.csv" if file_type == "2" else "transactions_excel.xlsx"
        )
        file_path = os.path.join(os.path.dirname(__file__), "../data", file_name)

        try:
            transactions = reader(str(file_path))

        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return
        if file_type == "1":
            transactions = convert_transaction(transactions)
        print("\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = input().upper().strip()

        filtered = filter_by_state(transactions, state)
        if not filtered:
            print(f"Нет операций с указанным статусом {state}.")
            return

        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
        if sort_choice == "да":
            order = input("Отсортировать по возрастанию или по убыванию? ").lower()
            filtered = sort_by_date(filtered, reverse=order == "по убыванию")

        rub_only = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
        if rub_only == "да":
            filtered = [t for t in filtered if t.get("currency_code") == "RUB"]

        if input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower() == "да":
            keyword = input("Введите слово для поиска: ").strip()
            if keyword:
                filtered = filter_operations_by_description(filtered, keyword)
        if len(filtered):
            print("Распечатываю итоговый список транзакций...")
            for transaction in filtered:
                display_transaction(transaction)

            print(f"Всего найдено операций: {len(filtered)}")
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
