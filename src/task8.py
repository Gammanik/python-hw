import math


def primes(n):
    return [x for x in range(2, n)
            if all(x % xi != 0
                   for xi in range(2, int(math.sqrt(x)) + 1))]
