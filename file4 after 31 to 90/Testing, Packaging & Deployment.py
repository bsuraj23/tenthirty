#Testing, Packaging & Deployment
#61.Unit tests
import unittest

def add(a,b): return a+b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)

if __name__=="__main__":
    unittest.main()
#62.Mocking
from unittest.mock import Mock

db = Mock()
db.get_user.return_value = {"name":"Alice"}

print(db.get_user(1))
#63.Patch dependencies in unit tests
# mymodule.py
import requests
def get_data():
    return requests.get("http://example.com").text
from unittest.mock import patch

@patch('mymodule.requests.get')
def test_get_data(mock_get):
    mock_get.return_value.text = "fake"
    from mymodule import get_data
    assert get_data() == "fake"
#65.Parameterized tests
import pytest

@pytest.mark.parametrize("a,b,expected", [(1,2,3),(5,5,10)])
def test_add(a,b,expected):
    assert a+b==expected
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        for a,b,expected in [(1,2,3),(5,5,10)]:
            with self.subTest(a=a,b=b):
                self.assertEqual(a+b,expected)

