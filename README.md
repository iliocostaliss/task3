# BankMe.

## Описание:

BankMe - это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/iliocostaliss/task3.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Тестирование:

Тесты для всех модулей хранятся в пакете "tests" и названы по имени модулей.
Для запуска тестов используй команду pytest.

## Модуль generators.py

Добавлен новый модуль, который предоставляет функции для работы с транзакциями. 
Модуль включает в себя следующие функции:

filter_by_currency(transactions, currency): фильтрует транзакции по заданной валюте и возвращает итератор.

transaction_descriptions(transactions): генератор, который возвращает описание каждой операции по очереди.

card_number_generator(start, end): генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.

### Примеры использования:

# Пример использования filter_by_currency
usd_transactions = filter_by_currency(transactions, 'USD')
for transaction in usd_transactions:
    print(transaction)

# Пример использования transaction_descriptions
for description in transaction_descriptions(transactions):
    print(description)

# Пример использования card_number_generator
for card in card_number_generator(4000123456789010, 4000123456789015):
    print(card)

## Использование:

1. Убедитесь, что установлено последнее обновление банковского приложения.
2. Откройте приложение в вашем личном кабинете.
3. Смотрите список последних успешных операций, в которые включена вся нужная информация: даты, суммы,
назначение операции.

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).
