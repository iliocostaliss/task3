from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> Union[str]:
    """
    Функция маскировки номера банковской карты.
    Принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX.
    """
    card_number_str = str(card_number).replace(" ", "")
    if len(card_number_str) != 16 or not card_number_str.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"

    return masked_number


def get_mask_account(account_number: Union[str, int]) -> Union[str]:
    """
    Функция маскировки номера банковского счета.
    Принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX.
    """
    account_number_str = str(account_number)
    if len(account_number_str) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 символа")

    last_four_nums = account_number_str[-4:]
    masked_account = "**" + last_four_nums

    return masked_account
