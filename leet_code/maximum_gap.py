'''
164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
'''


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0

        gap = 0
        nums = sorted(nums)
        for i in xrange(1, len(nums)):
            gap = max(gap, nums[i] - nums[i - 1])
        return gap


s = Solution()
input = [100, 3, 2, 1]
print s.maximumGap(input)
