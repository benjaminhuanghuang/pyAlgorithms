'''
368. Largest Divisible Subset

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this
subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]

'''


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return []
        n = len(nums)
        if n <= 1:
            return nums

        nums.sort()
        dp, index = [1] * n, [-1] * n
        max_dp, max_index = 1, 0
        for i in xrange(n):
            for j in xrange(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    index[i] = j

            if max_dp < dp[i]:
                max_dp, max_index = dp[i], i

        ans = []
        while max_index != -1:
            ans.append(nums[max_index])
            max_index = index[max_index]
        return ans
