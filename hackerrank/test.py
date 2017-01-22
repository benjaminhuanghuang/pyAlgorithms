def partition(ar):
    p = ar[0]
    l = 1
    r = len(ar) - 1
    while True:
        while ar[r] > p:
            r -= 1
        while ar[l] < p and l < r:
            l += 1
        if l >= r:
            break
        ar[l], ar[r] = ar[r], ar[l]
        l += 1
        r -= 1
    if r != 0:
        ar[0], ar[r] = ar[r], ar[0]


input = [4, 5, 3, 7, 2]
partition(input)
print input
