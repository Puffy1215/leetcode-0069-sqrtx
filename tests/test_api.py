"""Tests API for solving problem Sqrt(x)"""

import random
from typing import Callable

import pytest

from leetcode_0069_sqrtx import api


@pytest.mark.parametrize(
    ["result", "x"],
    (
        [0, 0],
        [1, 1],
        [2, 4],
        [2, 8],
        [3, 9],
        [3, 10],
    ),
)
def test_sqrtx(result: int, x: int) -> None:
    """Tests solution for problem Sqrt(x)"""

    assert api.sqrtx(x) == result


@pytest.fixture
def x_rand() -> Callable[[], int]:
    """Fixture to generate random x"""

    def _x_rand() -> int:
        return random.randint(api.X_MIN, api.X_MAX)

    return _x_rand
