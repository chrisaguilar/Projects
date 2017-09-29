def next_factor(n):
    for i in range(2, n):
        if not n % i:
            return i
    return n


def prime_factors(n):
    if n < 2:
        return 'Invalid'

    factors = []

    while True:
        factor = next_factor(n)
        if factor == n:
            factors.append(n)
            break

        n //= factor
        factors.append(factor)

    return factors


for i in range(2, 10000):
    print(i, prime_factors(i))
