import math


def is_prime(num):
    if num <= 1:
        return False

    sqr = int(math.sqrt(num)) + 1  # +1 for num =2
    for i in range(2, sqr):
        if num % i == 0:
            return True
    return False


print is_prime(12)
