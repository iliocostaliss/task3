import re
from collections import Counter


def filter_operations_by_description(operations, search_string):
    """
    Функция фильтрует данные о банковских операциях и возвращает список словарей,
    у которых в описании есть указанная строка.
    """
    filtered_operations = []
    for operation in operations:
        description = operation.get("description", "")
        if re.search(search_string, description, re.IGNORECASE):
            filtered_operations.append(operation)
    return filtered_operations


def count_operations_by_category(operations, categories):
    """
    Функция считает количество операций в каждой категории.
    """
    category_count = Counter()
    for operation in operations:
        description = operation.get("description", "")
        for category in categories:
            if re.search(rf"\b{category}\w*\b", description, re.IGNORECASE):
                category_count[category] += 1
    return dict(category_count)
