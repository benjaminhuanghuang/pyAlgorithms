def quick_sort(ar):
    qsort_helper(ar, 0, len(ar) - 1)
    # for i in ar:
    #    print i, 


def qsort_helper(ar, low, high):
    if low >= high:
        return
    p = ar[low]
    l = low + 1
    r = high
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
    if r != low:
        ar[low], ar[r] = ar[r], ar[low]
    qsort_helper(ar, low, r - 1)
    qsort_helper(ar, r + 1, high)
    if high > low:
        print " ".join(map(str, ar[low:high + 1]))


nums = [5, 8, 1, 3, 7, 9, 2]
quick_sort(nums)
