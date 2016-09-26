'''
327. Count of Range Sum

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
'''


class Solution(object):
    def countRangeSum_niave(self, nums, lower, upper):
        answer = 0
        for i in xrange(len(nums)):
            sum = 0
            for j in xrange(i, len(nums)):
                sum += nums[j]
                if sum >= lower and sum <= upper:
                    answer += 1
        return answer

    # https://segmentfault.com/a/1190000005098134
    def countRangeSum_1(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        len = len(nums)
        sum = [0]  # sum[i] = sum of element[0 to i] sum[0] = 0
        ans = 0
        for i in xrange(len):
            ans = nums[i]
            a = ans - upper
            b = ans - lower


nums = [-2, 5, -1]
lower = -2
upper = 2

s = Solution()
print s.countRangeSum_niave(nums, lower, upper)
