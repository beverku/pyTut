"""Example module for showing example module usage.
"""

from typing import List


def fib(n: int) -> List[int]:
    """
    :param n: limit(inclusive) for last value in sequence
    :return: Fibonacci sequence where the last value is <= n
    """
    result = []
    a = 0
    b = 1
    while b <= n:
        result.append(b)
        prev = b
        b += a
        a = prev
    return result
