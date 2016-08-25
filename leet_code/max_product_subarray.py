'''
152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''


class Solution(object):
    # temp = positive
    # positive = max(num, positive * num, negative * num)
    # negative = min(num, temp * num, negative * num)
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive, negative = nums[0], nums[0]
        result = nums[0]
        for num in nums[1:]:
            # positive = max(num, positive * num, negative * num)
            # negative = min(num, positive * num, negative * num)
            positive, negative = max(num, positive * num, negative * num), min(num, positive * num, negative * num)
            result = max(result, positive)
        return result


s = Solution()
print s.maxProduct([-4, -3, -2])
