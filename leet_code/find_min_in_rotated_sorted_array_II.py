'''
154. Find Minimum in Rotated Sorted Array II

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

reference:
    http://bangbingsyb.blogspot.com/2014/11/leecode-find-minimum-in-rotated-sorted.html
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums, left, right):
        if left == right:
            return nums[left]
        if nums[left] < nums[right]:  # [left....right] are ordered
            return nums[left]
        mid = (left + right) >> 1
        return min(self.search(nums, left, mid), self.search(nums, mid + 1, right))


nums = [3, 1, 3]

s = Solution()
print s.findMin(nums)
