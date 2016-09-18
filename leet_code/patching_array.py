'''
330. Patching Array

Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number
in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of
patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.


reference:
    http://www.cnblogs.com/grandyang/p/5165821.html
'''


class Solution(object):
    # http://bookshadow.com/weblog/2016/01/27/leetcode-patching-array/
    # http://blog.csdn.net/liyuefeilong/article/details/50616268
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        curr_summary = 1
        idx, ans = 0, 0
        size = len(nums)
        while curr_summary <= n:
            if idx < size and nums[idx] <= curr_summary:
                curr_summary += nums[idx]
                idx += 1
            else:
                curr_summary <<= 1
                ans += 1
        return ans
