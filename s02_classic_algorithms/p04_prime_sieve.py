"""
Classic Algorithm 04: Sieve of Eratosthenes.

The sieve of Eratosthenes is one of the most efficient ways to find all of the
smaller primes (below 10 million or so).
"""


def sieve(limit):
    """Return a list of prime numbers up to limit using a prime sieve."""
    if limit <= 1:
        return 'Invalid!'

    limit += 1

    A = [i for i in range(2, limit)]
    composites = {j for i in range(2, limit) for j in range(i * 2, limit, i)}
    primes = [num for num in A if num not in composites]

    return primes


print(sieve(10))
print(sieve(100))
print(sieve(1000))
print(sieve(10000))
print(sieve(100000))
print(sieve(1000000))
print(sieve(10000000))
