from typing import Union
import logging

import os

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "..\\logs\\", "masks.log"), "w", "utf-8"
)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str, int]) -> Union[str]:
    """
    Функция маскировки номера банковской карты.
    Принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX.
    """
    card_number_str = str(card_number).replace(" ", "")
    card_type = ''
    card_number_str_clear = ''
    if not card_number_str.isdigit():
        for num in card_number_str:
            if not num.isdigit():
                card_type += num
            else:
                card_number_str_clear += num
        card_number_str = card_number_str_clear
    logger.debug("Проверяем формат номера карты")
    if len(card_number_str) != 16:
        logger.error("Некорректный номер карты!")
        raise ValueError("Номер карты должен содержать 16 цифр")
    masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    if card_type:
        card_type = card_type.strip()
        masked_number = f"{card_type} {masked_number}"

    return masked_number


print(get_mask_card_number("1234567812345678"))


def get_mask_account(account_number: Union[str, int]) -> Union[str]:
    """
    Функция маскировки номера банковского счета.
    Принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX.
    """
    account_number_str = str(account_number)
    logger.debug("Проверяем формат номера счёта")
    if len(account_number_str) < 4:
        logger.error("Некорректный номер!")
        raise ValueError("Номер счета должен содержать минимум 4 символа")
    if len(account_number_str) > 20:
        logger.warning("Номер счёта слишком длинный!")
        raise ValueError("Номер счёта слишком длинный. Проверьте правильность набранного счёта.")

    last_four_nums = account_number_str[-4:]
    masked_account = "**" + last_four_nums

    return masked_account


print(get_mask_account("123456781234567812345678"))
