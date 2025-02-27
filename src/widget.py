from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: Union[str]) -> Union[str]:
    """
    Функция, которая умеет обрабатывать информацию как о картах, так и о счетах.
    Принимает на вход строку, содержащую тип (карту или счет) и подбирает подходящую под этот тип маскировку.
    """
    if account_info.startswith("Счет"):
        account_number = account_info[:5].replace(" ", "")
        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"

    else:
        card_number_parts = account_info.split()
        card_number = card_number_parts[-1]
        masked_number = get_mask_card_number(card_number)
        return " ".join(card_number_parts[-1] + masked_number)


def get_date(date_str: Union[str]) -> Union[str]:
    """
    Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    date_part = date_str.split("T")[0]
    day, month, year = date_part.split("-")
    formatted_date = f"{day},{month},{year}"
    return formatted_date
