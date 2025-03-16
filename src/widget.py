from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: Union[str]) -> Union[str]:
    """
    Функция, которая умеет обрабатывать информацию как о картах, так и о счетах.
    Принимает на вход строку, содержащую тип (карту или счет) и подбирает подходящую под этот тип маскировку.
    """
    if not account_info:
        raise ValueError("Введите номер карты или счёта!")

    if account_info.startswith("Счет"):
        account_number = account_info[5:].replace(" ", "")
        if not account_number.isdigit():
            raise ValueError("Номер счёта должен состоять из цифр!")

        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"

    else:
        card_number_parts = account_info.split()
        if len(card_number_parts) < 2:
            raise ValueError("Некорректный формат ввода!")

        card_type = " ".join(card_number_parts[:-1])
        card_number = card_number_parts[-1]
        card_number_clear = ""
        for num in card_number:
            if num.isdigit():
                card_number_clear += num
        if not card_number_clear.isdigit():
            raise ValueError("Номер карты должен состоять из цифр!")

        masked_number = get_mask_card_number(card_number_clear)
        return f"{card_type} {masked_number}"


def get_date(date_str: Union[str]) -> Union[str]:
    """
    Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    if not date_str:
        return "Введите дату."
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date
