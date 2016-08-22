'''
300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''


class Solution(object):
    # dp[i] = l
    def lengthOfLIS_n2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or not nums:
            return 0
        dp = [1] * len(nums)
        for curr, val in enumerate(nums):
            for prev in xrange(curr):
                if nums[prev] < val:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
        return max(dp)
