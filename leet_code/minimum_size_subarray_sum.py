'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a subarray
of which the sum >= s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''


class Solution(object):
    # http://blog.csdn.net/lisonglisonglisong/article/details/45666975
    # if total < s, extend right
    # if total >=s, extend left
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0:
            return 0
        left = right = total = 0
        ans = n + 1
        while right < n:
            while right < n and total < s:
                total += nums[right]
                right += 1
            if total < s:
                break
            while left < right and total >= s:
                total -= nums[left]
                left += 1
            ans = min(ans, right - left + 1)

        if ans == n + 1:
            return 0
        else:
            return ans


array = [2, 3, 1, 2, 4, 3]
s = 7

sol = Solution()
print sol.minSubArrayLen(s, array)
