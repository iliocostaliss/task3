from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> Union[str]:
    """
    Функция маскировки номера банковской карты.
    Принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX.
    """
    card_number_str = str(card_number).replace(" ", "")
    card_type = ''
    card_number_str_cleaned = ''
    if not card_number_str.isdigit():
        for num in card_number_str:
            if not num.isdigit():
                card_type += num
            else:
                card_number_str_cleaned += num
        card_number_str = card_number_str_cleaned
    if len(card_number_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    if card_type:
        card_type = card_type.strip()
        masked_number = f"{card_type} {masked_number}"

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
    if len(account_number_str) > 20:
        raise ValueError("Номер счёта слишком длинный. Проверьте правильность набранного счёта.")

    last_four_nums = account_number_str[-4:]
    masked_account = "**" + last_four_nums

    return masked_account
