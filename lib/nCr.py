from math import factorial
from itertools import accumulate
from operator import mul


def nCr(n, r):
    if r > n or r < 0:
        return 0
    if r == n or r == 0:
        return 1
    a, b = max(r, n - r), min(r, n - r)
    a = list(accumulate(range(a + 1, n + 1), mul))[-1]
    return a // factorial(b)
