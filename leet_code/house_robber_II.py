'''
213. House Robber II

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will
not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house
is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the
previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Reference
    http://www.cnblogs.com/grandyang/p/4518674.html
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])

        return max(self.dfs(nums[1:]), self.dfs(nums[:-1]))

    def dfs(self, nums):
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0 for each in nums]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for index in xrange(2, len(nums)):
            dp[index] = max(dp[index - 2] + nums[index], dp[index - 1])
        return dp[- 1]
