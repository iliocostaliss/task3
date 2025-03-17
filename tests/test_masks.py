import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_standard_card_number():
    card_number = "1234 5678 1234 5678"
    assert get_mask_card_number(card_number) == "1234 56** **** 5678"


@pytest.mark.parametrize(
    "card_number, expected_error_message",
    [
        ("1234", "Номер карты должен содержать 16 цифр"),
        ("1234 5678 9012 3456 7890", "Номер карты должен содержать 16 цифр"),
        ("1234 card 5678 card", "Номер карты должен содержать 16 цифр"),
    ],
)
def test_card_number_length(card_number, expected_error_message):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
    assert str(exc_info.value) == expected_error_message


def test_standard_account_number():
    standard_account_number = "12345678901234567890"
    assert get_mask_account(standard_account_number) == "**7890"


def test_short_account_number():
    short_account_number = "123"
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(short_account_number)
    assert str(exc_info.value) == "Номер счета должен содержать минимум 4 символа"


def test_long_account_number():
    with pytest.raises(ValueError):
        assert get_mask_account("123456789012345678901234567890")


def test_empty_input():
    with pytest.raises(ValueError):
        assert get_mask_account("")
