def fibonacci(n):
    # Write your code here.
    if n == 0:
        return 0
    if n == 1:
        return 1
    n0 = 0
    n1 = 1
    f = 0
    for i in range (2, n + 1, 1):
        f = n0 + n1
        print f
        n0 = n1
        n1 = f
    return f


n = 5
print fibonacci(n)
