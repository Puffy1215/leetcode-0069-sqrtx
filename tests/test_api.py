"""Tests API for solving problem Sqrt(x)"""

import pytest

from leetcode_0069_sqrtx import api


@pytest.mark.parametrize(
    ["result", "x"],
    (
        [2, 4],
        [2, 8],
    ),
)
def test_sqrtx(result, x) -> None:
    """Tests solution for problem Sqrt(x)"""

    assert api.sqrtx(x) == result
