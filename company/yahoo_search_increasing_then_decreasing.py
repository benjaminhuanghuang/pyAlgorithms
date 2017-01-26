'''
Given an array which is having elements which are in increasing order till a max value and then numbers in decreasing order.

162. Find Peak Element
'''


def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, r = 0, len(nums) - 1

    while l < r:
        mid = l + (r - l) / 2

        if nums[mid] >= nums[mid + 1]:
            r = mid
        else:
            l = mid + 1

    return l


