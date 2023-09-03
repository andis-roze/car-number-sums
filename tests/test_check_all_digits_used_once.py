import pytest
from typing import NamedTuple

from main import check_all_digits_used_once


class TestCaseParameters(NamedTuple):
    number: str
    operands: list
    expected: bool


test_cases = [
    ("0138", ["0", "3", "8", "1"], True),
    ("0138", ["3", "8", "1"], True),
    ("0138", ["0", "3", "3", "1"], False),
    ("0138", ["3", "3", "1"], False),
    ("2345", ["2", "3", "4", "5"], True),
    ("2345", ["23", "4", "5"], True),
    ("2345", ["234", "5"], True),
    ("2345", ["235", "5"], False),
    ("2345", ["234", "45"], False),
    ("2345", ["24", "4", "5"], False),
    ("2345", ["2", "34", "5"], True),
    ("2345", ["2", "345"], True),
    ("2345", ["23", "345"], False),
    ("2345", ["2", "2345"], False),
    ("2345", ["2", "35", "5"], False),
    ("2345", ["2", "3", "45"], True),
    ("2345", ["2", "3", "55"], False),
    ("2345", ["234", "5"], True),
    ("2345", ["2", "345"], True),
    ("2345", ["2345"], True),
]


@pytest.mark.parametrize("test_case", test_cases)
def test_check_number_has_enough_digits(test_case):
    params = TestCaseParameters(*test_case)
    assert check_all_digits_used_once(params.number, params.operands) == params.expected
