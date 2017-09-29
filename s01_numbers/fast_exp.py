from time import time

def exponentiate(x, n):
    if n < 0: return exponentiate(1 / x, -n)
    elif n == 0: return 1
    elif n == 1: return x
    elif not n % 2: return exponentiate(x * x, n / 2)
    elif n % 2: return x * exponentiate(x * x, (n - 1) / 2)

start = time()
exponentiate(123456789, 5000000)
print(time() - start)

start = time()
123456789 ** 5000000
print(time() - start)
