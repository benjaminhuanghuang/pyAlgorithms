def quick_sort(ar):
    if not len or len(ar) < 2:
        return ar
    pivot = ar[0]
    left = []
    right = []

    for i in range(1, len(ar)):
        if ar[i] < pivot:
            left.append(ar[i])
        else:
            right.append(ar[i])

    left = quick_sort(left)
    right = quick_sort(right)

    if left:
        s = left + [pivot]
        if right:
            s = s + right
    else:
        s = [pivot]
        if right:
            s = s + right

    if len(ar) > 1:
        print " ".join(map(str, s))
    return s


def partition(ar):
    pivot = ar[0]
    left = []
    right = []

    for i in range(1, len(ar)):
        if ar[i] < pivot:
            left.append(ar[i])
        else:
            right.append(ar[i])

    ar[:] = left + [pivot] + right


nums = [5, 8, 1, 3, 7, 9, 2]
s = quick_sort(nums)
print s
