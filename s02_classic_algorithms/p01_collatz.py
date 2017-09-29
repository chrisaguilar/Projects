"""
Classic Algorithm 01: Collatz Conjecture.

Start with a number n > 1. Find the number of steps it takes to reach one using
the following process: If n is even, divide it by 2. If n is odd, multiply it
by 3 and add 1.
"""

from typing import List


def collatz(num: int) -> List[int]:
    """Return the collatz sequence for the given integer."""
    seq: List = []
    while num != 1:
        num = (num // 2) if (not num % 2) else (3 * num + 1)
        seq.append(num)

    return seq


for i in range(2, 1001):
    print(i, collatz(i))
