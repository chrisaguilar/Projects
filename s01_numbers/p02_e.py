"""
Calculates e to n digits.
"""
from decimal import Decimal as D, getcontext
from math import factorial

# VERY SLOW, math.factorial is MUCH, MUCH faster
# def factorial(n):
#     """Given n, returns n!."""
#     return 1 if n <= 0 else n * factorial(n - 1)


def e(n):
    """
    Calculate Euler's Number (e) to n digits.

    https://en.wikipedia.org/wiki/E_(mathematical_constant)
    """
    if n > 10000:
        print('Not a good idea, you\'ll regret it. Try a lower number.')
        return
    getcontext().prec = n
    return sum(D(1 / factorial(x)) for x in range(n))


print(e(10))
print(e(100))
print(e(1000))
print(e(10000))
