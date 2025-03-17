from src.processing import filter_by_state
import pytest


@pytest.fixture
def state_value():
    return [
        {"id": 41428829, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED"},
        {"id": 615064591, "state": "CANCELED"},
    ]


@pytest.fixture
def date_sort():
    return [
        {"id": 41428829, 'date': '2019-07-03T18:35:29.512364'},
        {"id": 939719570, 'date': '2018-06-30T02:08:58.425572'},
        {"id": 594226727, 'date': '2018-09-12T21:27:25.241689'},
        {"id": 615064591, 'date': '2018-10-14T08:21:33.419441'},
    ]


@pytest.fixture
def date_same():
    return [
        {"id": 41428829, 'date': '2019-07-03T18:35:29.512364'},
        {"id": 939719570, 'date': '2018-06-30T02:08:58.425572'},
        {"id": 594226727, 'date': '2018-09-12T21:27:25.241689'},
        {"id": 615064591, 'date': '2018-10-14T08:21:33.419441'},
        {"id": 594226727, 'date': '2018-09-12T21:27:25.241689'}, #id 3
        {"id": 41428829, 'date': '2019-07-03T18:35:29.512364'},  #id 1
        {"id": 615064591, 'date': '2018-10-14T08:21:33.419441'}, #id 4
    ]


@pytest.fixture
def invalid_date():
    return [
        {"id": 41428829, 'date': '2019-07-03'},
        {"id": 939719570, 'date': ''},
        {"id": 594226727, 'date': '2018/09/12'},
        {"id": 615064591, 'date': '2018-10-14T08:21:AB.ABCD'},
    ]