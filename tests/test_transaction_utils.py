from src.transaction_utils import count_operations_by_category, filter_operations_by_description


def test_filter_operations_by_description(description_transactions):
    filtered = filter_operations_by_description(description_transactions, "перевод")
    assert all("перевод" in t["description"].lower() for t in filtered)


def test_empty_dict():
    result = filter_operations_by_description([], "перевод")
    assert len(result) == 0


def test_no_matches(description_transactions):
    result = filter_operations_by_description(description_transactions, "несуществующееописание")
    assert len(result) == 0


def test_count_operations_by_category(count_categories):
    categories = ["Перевод организации", "Открытие вклада"]
    result = count_operations_by_category(count_categories, categories)
    assert result == {"Перевод организации": 2, "Открытие вклада": 3}


def test_empty_categories(count_categories):
    categories = []
    result = count_operations_by_category(count_categories, categories)
    assert result == {}
