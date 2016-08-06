def binary_search(nums, x):
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) >> 1
        if nums[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return low
