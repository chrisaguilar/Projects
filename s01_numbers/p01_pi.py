"""
Calculates pi to n digits using Bellard's Formula.

https://en.wikipedia.org/wiki/Bellard%27s_formula
"""
from decimal import Decimal as D
from decimal import getcontext


def fun(n):
    a = D(-1)**n / 1024**n
    b = D(32) / (4 * n + 1)
    c = D(1) / (4 * n + 3)
    d = D(256) / (10 * n + 1)
    e = D(64) / (10 * n + 3)
    f = D(4) / (10 * n + 5)
    g = D(4) / (10 * n + 7)
    h = D(1) / (10 * n + 9)

    return a * -(b + c - d + e + f + g - h)


def pi(n):
    if n > 1000:
        print('Not a good idea, you\'ll regret it. Try a lower number.')
        return
    getcontext().prec = n
    return D(1 / 64) * sum([fun(x) for x in range(n)])


print(pi(3))
print(pi(9))
print(pi(10))
print(pi(100))
print(pi(1000))
