import os
from unittest.mock import patch

import pytest
import requests

from src.external_api import convert_to_rub


def test_convert_rub_to_rub():
    result = convert_to_rub(20, "RUB")
    assert result == 20


def test_convert_usd_to_rub():
    with patch("src.external_api.requests.get") as mock_get:
        fake_api_response = {
            "success": True,
            "query": {"from": "USD", "to": "RUB", "amount": 100},
            "info": {"rate": 84.66},
            "result": 8466.0
        }
        mock_get.return_value.json.return_value = fake_api_response
        result = convert_to_rub(100, "USD")
        assert result == 8466.0
        expected_url = "https://api.apilayer.com/exchangerates_data/convert"
        mock_get.assert_called_once_with(
            expected_url,
            params={"to": "RUB", "from": "USD", "amount": 100},
            headers={"apikey": os.getenv("API_KEY")},
            timeout=10
        )


def test_convert_with_api_error():
    with patch("src.external_api.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("API недоступно")

        try:
            convert_to_rub(100, "EUR")
            pytest.fail("ValueError")
        except ValueError as e:
            assert "API недоступно" in str(e)


def test_api_connection_error():
    with patch("src.external_api.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError("Не удалось подключиться к API")
        with pytest.raises(ValueError) as exc_info:
            convert_to_rub(100, "USD")

        assert "Не удалось подключиться к API" in str(exc_info.value)
