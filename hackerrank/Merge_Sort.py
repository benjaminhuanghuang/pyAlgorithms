def count_inversions(nums):
    return merge_sort(nums, 0, len(nums) - 1)


def merge_sort(nums, l, r):
    if l == r:
        return 0
    mid = l + (r - l) / 2
    count = 0
    count += merge_sort(nums, l, mid)
    count += merge_sort(nums, mid + 1, r)
    count += merge(nums, l, r)
    return count


def merge(nums, l, r):
    mid = l + (r - l) / 2
    res = []
    count = 0
    i = l
    j = mid + 1
    while (i <= mid and j <= r):
        if nums[i] > nums[j]:
            res.append(nums[j])
            count += mid - i + 1  # Tricky part
            j += 1
        else:
            res.append(nums[i])
            i += 1
    while (i <= mid):
        res.append(nums[i])
        i += 1
    while (j <= r):
        res.append(nums[j])
        j += 1
    for i in range(r+1-l):
        nums[l+i] = res[i]
    return count


print count_inversions([1, 1, 1, 2, 2])
print count_inversions([2, 1, 3, 1, 2])