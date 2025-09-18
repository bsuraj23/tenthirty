#63.How do you patch dependencies in unit tests (`unittest.mock`)?
from unittest.mock import patch

# Code under test
import requests

def fetch_data(url):
    return requests.get(url).json()

# Test
@patch("requests.get")
def test_fetch_data(mock_get):
    mock_get.return_value.json.return_value = {"key": "value"}

    result = fetch_data("http://fake.url")
    assert result == {"key": "value"}
    mock_get.assert_called_once_with("http://fake.url")
