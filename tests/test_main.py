from unittest.mock import patch

from src.main import convert_transaction, get_file_reader, main, read_transactions_csv, read_transactions_excel


def test_get_file_reader():
    assert callable(get_file_reader("1"))
    assert callable(get_file_reader("2"))
    assert callable(get_file_reader("3"))


def test_convert_transaction_empty():
    result = convert_transaction([])
    assert result == []


@patch("csv.DictReader")
@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_transactions_csv_file_not_found(mock_open_file, mock_csv):
    result = read_transactions_csv("nonexistent.csv")
    assert result == []
    assert mock_open_file.call_args[0] == ("nonexistent.csv", "r")
    assert mock_open_file.call_args[1]["encoding"] == "utf-8"


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_read_transactions_excel_not_found(mock_read_excel):
    result = read_transactions_excel("missing.xlsx")
    assert result == []
    mock_read_excel.assert_called_once_with("missing.xlsx")


@patch("src.main.get_file_reader")
def test_main_with_no_transactions_after_filter(mock_get_reader):
    mock_get_reader.return_value = lambda x: [{"id": 1, "state": "PENDING"}]
    with patch("builtins.input", side_effect=["1", "EXECUTED"]):
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_called_with("Нет операций с указанным статусом EXECUTED.")


@patch("src.main.get_file_reader")
def test_main_with_invalid_file_type(mock_get_reader):
    mock_get_reader.return_value = None
    with patch("builtins.input", return_value="4"):
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_called_with("Неверный выбор файла. Программа завершена.")
