import pytest
from typing import NamedTuple

from main import get_operands


class TestCaseParameters(NamedTuple):
    number: str
    expected: list


test_cases = [
    (
        "0578",
        [
            [578],
            [587],
            [758],
            [785],
            [857],
            [875],
            [5078],
            [5087],
            [5708],
            [5780],
            [5807],
            [5870],
            [7058],
            [7085],
            [7508],
            [7580],
            [7805],
            [7850],
            [8057],
            [8075],
            [8507],
            [8570],
            [8705],
            [8750],
            [5, 78],
            [5, 87],
            [7, 58],
            [7, 85],
            [8, 57],
            [8, 75],
            [5, 708],
            [5, 780],
            [5, 807],
            [5, 870],
            [7, 508],
            [7, 580],
            [7, 805],
            [7, 850],
            [8, 507],
            [8, 570],
            [8, 705],
            [8, 750],
            [50, 78],
            [50, 87],
            [57, 80],
            [58, 70],
            [70, 58],
            [70, 85],
            [75, 80],
            [78, 50],
            [80, 57],
            [80, 75],
            [85, 70],
            [87, 50],
            [5, 7, 8],
            [5, 8, 7],
            [7, 5, 8],
            [7, 8, 5],
            [8, 5, 7],
            [8, 7, 5],
            [5, 7, 80],
            [5, 8, 70],
            [7, 5, 80],
            [7, 8, 50],
            [8, 5, 70],
            [8, 7, 50],
        ],
    ),
    (
        "0138",
        [
            [138],
            [183],
            [318],
            [381],
            [813],
            [831],
            [1038],
            [1083],
            [1308],
            [1380],
            [1803],
            [1830],
            [3018],
            [3081],
            [3108],
            [3180],
            [3801],
            [3810],
            [8013],
            [8031],
            [8103],
            [8130],
            [8301],
            [8310],
            [1, 38],
            [1, 83],
            [3, 18],
            [3, 81],
            [8, 13],
            [8, 31],
            [1, 308],
            [1, 380],
            [1, 803],
            [1, 830],
            [3, 108],
            [3, 180],
            [3, 801],
            [3, 810],
            [8, 103],
            [8, 130],
            [8, 301],
            [8, 310],
            [10, 38],
            [10, 83],
            [13, 80],
            [18, 30],
            [30, 18],
            [30, 81],
            [31, 80],
            [38, 10],
            [80, 13],
            [80, 31],
            [81, 30],
            [83, 10],
            [1, 3, 8],
            [1, 8, 3],
            [3, 1, 8],
            [3, 8, 1],
            [8, 1, 3],
            [8, 3, 1],
            [1, 3, 80],
            [1, 8, 30],
            [3, 1, 80],
            [3, 8, 10],
            [8, 1, 30],
            [8, 3, 10],
        ],
    ),
    ("01", [[1], [10]]),
    ("12", [[12], [21], [1, 2], [2, 1]]),
    ("012", [[12], [21], [102], [120], [201], [210], [1, 2], [2, 1], [1, 20], [2, 10]]),
    (
        "123",
        [
            [123],
            [132],
            [213],
            [231],
            [312],
            [321],
            [1, 23],
            [1, 32],
            [2, 13],
            [2, 31],
            [3, 12],
            [3, 21],
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ],
    ),
    (
        "0123",
        [
            [123],
            [132],
            [213],
            [231],
            [312],
            [321],
            [1023],
            [1032],
            [1203],
            [1230],
            [1302],
            [1320],
            [2013],
            [2031],
            [2103],
            [2130],
            [2301],
            [2310],
            [3012],
            [3021],
            [3102],
            [3120],
            [3201],
            [3210],
            [1, 23],
            [1, 32],
            [2, 13],
            [2, 31],
            [3, 12],
            [3, 21],
            [1, 203],
            [1, 230],
            [1, 302],
            [1, 320],
            [2, 103],
            [2, 130],
            [2, 301],
            [2, 310],
            [3, 102],
            [3, 120],
            [3, 201],
            [3, 210],
            [10, 23],
            [10, 32],
            [12, 30],
            [13, 20],
            [20, 13],
            [20, 31],
            [21, 30],
            [23, 10],
            [30, 12],
            [30, 21],
            [31, 20],
            [32, 10],
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
            [1, 2, 30],
            [1, 3, 20],
            [2, 1, 30],
            [2, 3, 10],
            [3, 1, 20],
            [3, 2, 10],
        ],
    ),
]


@pytest.mark.parametrize("test_case", test_cases)
def test_get_operands(test_case):
    params = TestCaseParameters(*test_case)
    operand_combinations = get_operands(params.number)

    assert operand_combinations == params.expected