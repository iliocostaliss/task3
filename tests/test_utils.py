import json
from unittest.mock import mock_open, patch

from src.utils import dict_transactions


def test_dict_transactions():
    fake_transactions = [
        {"id": 123456789, "amount": 123.321},
        {"id": 234567890, "amount": 4567.89},
        {"id": 567891234, "amount": 890.98},
    ]

    with patch("builtins.open", mock_open()):
        with patch("json.load", return_value=fake_transactions):
            result = dict_transactions("test_file.json")

            assert result == fake_transactions


def test_empty_dict_transactions():
    with patch("builtins.open", mock_open(read_data="")) as mock_open_file:
        with patch("json.load", side_effect=json.JSONDecodeError("Empty file", "", 0)):
            result = dict_transactions("empty.json")
            assert result == []
            mock_open_file.assert_called_once_with("empty.json", "r", encoding="utf-8")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_dict_transactions_file_not_found(mock_file):
    result = dict_transactions("file_not_found.json")
    assert result == []
    mock_file.assert_called_once_with("file_not_found.json", "r", encoding="utf-8")
