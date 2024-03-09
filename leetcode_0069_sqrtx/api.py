"""API for solving problem Sqrt(x)"""

from math import ceil, floor

X_MAX = 2**31 - 1
X_MIN = 0


def _check_preconditions(x: int) -> bool:
    if x < 0:
        return False

    if not X_MIN <= x <= X_MAX:
        return False

    return True


def sqrtx(x: int) -> int:
    """Solves problem Sqrt(x)"""

    assert _check_preconditions(x)

    lower = 0
    upper = x

    while upper != lower:
        middle = (upper + lower) / 2
        if x < middle * middle:
            upper = floor(middle)
        else:
            lower = ceil(middle)

    return lower
