from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_standard_card_number():
    card_number = "1234 5678 1234 5678"
    assert get_mask_card_number(card_number) == "1234 56** **** 5678"


def test_short_card_number():
    short_card_number = "1234"
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(short_card_number)
    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр"


def test_long_card_number():
    long_card_number = "1234 5678 9012 3456 7890"
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(long_card_number)
    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр"


def test_letters_card_number():
    letters_card_number = "1234 card 5678 card"
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(letters_card_number)
    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр"


def test_empty_card_number():
    with pytest.raises(ValueError):
        assert get_mask_card_number("")


def test_standard_account_number():
    standard_account_number = "123456"
    assert  get_mask_account(standard_account_number) == "**3456"


def test_short_account_number():
    short_account_number = "123"
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(short_account_number)
    assert str(exc_info.value) == "Номер счета должен содержать минимум 4 символа"


def test_empty_account_number():
    with pytest.raises(ValueError):
        assert get_mask_account("")




