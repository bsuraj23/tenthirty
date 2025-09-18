#65.How do you write a parameterized test in Python?
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 5, 5)
])
def test_add(a, b, expected):
    assert a + b == expected


