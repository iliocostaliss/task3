import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED"},
                {"id": 939719570, "state": "EXECUTED"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED"},
                {"id": 615064591, "state": "CANCELED"},
            ],
        ),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(state_value, state, expected):
    result = filter_by_state(state_value, state)
    assert result == expected


def test_filter_by_state_empty():
    assert filter_by_state([], "EXECUTED") == []


def test_filter_by_state_unknown(state_value):
    expected_result = []
    result = filter_by_state(state_value, "UNKNOWN")
    assert result == expected_result


@pytest.mark.parametrize(
    "reverse, expected",
    [
        (True, [41428829, 615064591, 594226727, 939719570]),
        (False, [939719570, 594226727, 615064591, 41428829]),
    ],
)
def test_sort_by_date(date_sort, reverse, expected):
    result = sort_by_date(date_sort, reverse)
    result_id = [item["id"] for item in result]
    assert result_id == expected


def test_sort_same_dates(date_same):
    result = sort_by_date(date_same, reverse=True)
    expected_id = [41428829, 41428829, 615064591, 615064591, 594226727, 594226727, 939719570]
    result_id = [item["id"] for item in result]
    assert result_id == expected_id


def test_invalid_date(invalid_date):
    result = sort_by_date(invalid_date)
    result_id = [item["id"] for item in result]
    expected_id = [41428829, 939719570, 594226727, 615064591]
    assert set(result_id) == set(expected_id)
