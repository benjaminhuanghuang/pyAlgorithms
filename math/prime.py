def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_2(n):
    for i in range(2, n / 2 + 1):
        if n % i == 0:
            return False
    return True


for i in xrange(10000):
    if is_prime(i) == is_prime_2(i):
        pass
        print "pass ", i
    else:
        print "not pass ", i
