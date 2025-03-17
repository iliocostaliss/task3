from src.widget import mask_account_card, get_date
import pytest


def test_recognize_account():
    account_number = "Счет 12345678901234567890"
    result = mask_account_card(account_number)
    assert result.startswith("Счет")


def test_mask_account():
    account_number = "Счет 12345678901234567890"
    assert mask_account_card(account_number) == "Счет **7890"


def test_invalid_account_number():
    invalid_account_number = "Счет 12345ABCD"
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(invalid_account_number)
    assert str(exc_info.value) == "Номер счёта должен состоять из цифр!"


def test_empty_input():
    with pytest.raises(ValueError):
        assert mask_account_card("")


def test_correct_mask_card():
    card_number = "Visa 1234567890123456"
    assert mask_account_card(card_number) == "Visa 1234 56** **** 3456"


def test_invalid_card_number():
    invalid_card_number = "MasterCard 1234 ABCD 5678 EFGH"
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(invalid_card_number)
    assert str(exc_info.value) == "Номер карты должен состоять из цифр!"


@pytest.mark.parametrize("card_number, expected_mask", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")
])
def test_different_cards(card_number, expected_mask):
    assert mask_account_card(card_number) == expected_mask


def test_standard_date():
    date = "2024-03-11T02:26:18.671407"
    assert get_date(date) == "11.03.2024"


def test_short_date():
    date = "2024-03-11"
    assert get_date(date) == "11.03.2024"


def test_empty_date():
    date = ""
    assert get_date(date) == "Введите дату."

