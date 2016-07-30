'''
26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question

'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) <= 0:
            return nums
        size = 0
        for i in xrange(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[size] = nums[i]
                size += 1
        return size


nums = [1, 1, 1, 1, 2, 3, 3, 4, 5]

s = Solution()
print s.removeDuplicates(nums)
