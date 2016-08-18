'''
33. Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

'''


class Solution(object):
    # http://www.cnblogs.com/Dabay/p/4269053.html
    # if mid > left, means left side is raising
    #   if target in left section, search left, or search right
    # if mid < left,
    #   if target in right section, search left, or search right
    def search_bs(self, nums, target):
        if len(nums) == 1:
            return [-1, 0][nums[0] == target]

        if nums[0] == target:
            return 0
        elif nums[0] < target:
            i = 1
            while i < len(nums) and nums[i - 1] < nums[i] and nums[i - 1] < target:
                if nums[i] == target:
                    return i
                i = i + 1
            else:
                return -1
        else:
            if nums[-1] == target:
                return len(nums) - 1
            i = len(nums) - 2
            while i >= 0 and nums[i] < nums[i + 1] and target < nums[i + 1]:
                if nums[i] == target:
                    return i
                i = i - 1
            else:
                return -1

    # http://www.cnblogs.com/Dabay/p/4269053.html
    # if target < first num, search nums from left to right
    # if target > fist num, search nums from right to left
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            m = (left + right) / 2
            mid = nums[m]
            if mid == target:
                return m
            if mid > nums[left]:
                if nums[left] < target and target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:
                if nums[m] < target and target < nums[right]:
                    left = m + 1
                else:
                    right = m - 1
        else:
            return -1
