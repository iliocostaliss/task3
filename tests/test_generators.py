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


def test_generator_range():
    """Тестирование функции card_number_generator"""
    expected_result = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]
    assert list(card_number_generator(1, 4)) == expected_result


def test_card_number_generator():
    card_number = next(card_number_generator(5, 5))
    assert card_number == "0000 0000 0000 0005"
    assert len(card_number) == 19
    assert all(len(groups) == 4 and groups.isdigit() for groups in card_number.split())


def test_border_value():
    assert next(card_number_generator(1, 1)) == "0000 0000 0000 0001"
    max_value = card_number_generator(9999999999999999, 9999999999999999)
    assert next(max_value) == "9999 9999 9999 9999"
    with pytest.raises(StopIteration):
        next(max_value)


def test_empty_card_number():
    with pytest.raises(StopIteration):
        next(card_number_generator(5, 1))