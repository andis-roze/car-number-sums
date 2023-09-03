import pytest
from typing import NamedTuple

from main import build_expressions


class TestCaseParameters(NamedTuple):
    operands: list
    expected_expressions: dict


test_cases = [
    (
        [3, 8, 1],
        {
            "3+8+1": 12,
            "3+8-1": 10,
            "3+8*1": 11,
            "3+8/1": 11.0,
            "3-8+1": -4,
            "3-8-1": -6,
            "3-8*1": -5,
            "3-8/1": -5.0,
            "3*8+1": 25,
            "3*8-1": 23,
            "3*8*1": 24,
            "3*8/1": 24.0,
            "3/8+1": 1.375,
            "3/8-1": -0.625,
            "3/8*1": 0.375,
            "3/8/1": 0.375,
        },
    ),
    (
        [7, 8, 5],
        {
            "7+8+5": 20,
            "7+8-5": 10,
            "7+8*5": 47,
            "7+8/5": 8.6,
            "7-8+5": 4,
            "7-8-5": -6,
            "7-8*5": -33,
            "7-8/5": 5.4,
            "7*8+5": 61,
            "7*8-5": 51,
            "7*8*5": 280,
            "7*8/5": 11.2,
            "7/8+5": 5.875,
            "7/8-5": -4.125,
            "7/8*5": 4.375,
            "7/8/5": 0.175,
        },
    ),
]


@pytest.mark.parametrize("test_case", test_cases)
def test_build_expressions(test_case):
    params = TestCaseParameters(*test_case)
    expressions = build_expressions([params.operands])
    print(expressions)
    assert expressions == params.expected_expressions
