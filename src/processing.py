from typing import Iterable, Dict, Any, List


def filter_by_state(list_dict: Iterable[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """
    filtered_dict = []
    for item in list_dict:
        if item.get("state") == state:
            filtered_dict.append(item)

    return filtered_dict


def sort_by_date(list_dict: Iterable[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:

    return sorted(list_dict, key=lambda x: x["date"])

