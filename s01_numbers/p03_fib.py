from time import time


def fib(n):
    start = time()
    if n > 1000000:
        print('Not a good idea, you\'ll regret it. Try a lower number.')
        return
    a, b = 1, 0
    for i in range(1, n + 1):
        a, b = b, a + b
    print(f'\nTime Elapsed: {time() - start}')
    return b


print(fib(1))
print(fib(10))
print(fib(100))
print(fib(1000))
print(fib(10000))
print(fib(100000))
print(fib(1000000))
