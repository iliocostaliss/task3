from src.widget import mask_account_card, get_date
import pytest


def is_account_number():
    account_number_start = "Счет"
    assert  mask_account_card(account_number_start) == "**7890"


def is_digit_account_number():
    account_number = "1234card5678card1234"
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(account_number)
    assert str(exc_info.value) == "Номер счёта должен состоять из цифр!"


def is_digit_card_number():
    card_number = "1234 card 1234 card"
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(card_number)
    assert str(exc_info.value) == "Номер карты должен состоять из цифр!"



