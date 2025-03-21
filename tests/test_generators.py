import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency, expected_result", [
    ("USD", "USD"),
    ("RUB", "RUB"),
    ("EUR", "EUR"),
])

def test_filter_by_currency(transactions, currency, expected_result):
    """Тестирование функции filter_by_currency"""
    filtered_transactions = list(filter_by_currency(transactions, currency))
    assert all(i["operationAmount"]["currency"]["code"] == expected_result for i in filtered_transactions)


def test_empty_list():
    assert len(list(filter_by_currency([], "EUR"))) == 0


def test_transaction_descriptions(transactions):
    """Тестирование функции transaction_descriptions"""
    description = transaction_descriptions(transactions)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(description)


def test_one_transaction(one_transaction):
    description = transaction_descriptions(one_transaction)
    assert next(description) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(description)


def test_empty_transaction(empty_transaction):
    description = transaction_descriptions(empty_transaction)
    with pytest.raises(StopIteration):
        next(description)
