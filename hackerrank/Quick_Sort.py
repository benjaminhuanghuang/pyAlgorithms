count = 0


def quick_sort_helper(nums, l, r):
    if l >= r:
        return nums
    temp = nums[l]
    i = l + 1
    j = r
    while True:
        while (nums[j] > temp):
            j -= 1
        while (nums[i] < temp):
            i += 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    if j != l:
        nums[j], nums[l] = nums[l], nums[j]
    quick_sort_helper(nums, j + 1, r)
    quick_sort_helper(nums, l, j - 1)


def quick_sort(nums):
    quick_sort_helper(nums, 0, len(nums) - 1)
