'''

If possible, try to come up with an O(sqr(n)) primality algorithm, or see what sort of optimizations
you can come up with for an O(n) algorithm.
'''
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True
