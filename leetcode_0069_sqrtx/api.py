"""API for solving problem Sqrt(x)"""

X_MAX = 2**31 - 1
X_MIN = 0


def _check_preconditions(x: int) -> bool:
    if x < 0:
        return False

    if X_MIN <= x <= X_MAX:
        return False

    return True


def sqrtx(x: int) -> int:
    """Solves problem Sqrt(x)"""

    assert _check_preconditions(x)

    pass
