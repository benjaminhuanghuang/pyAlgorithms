'''
153. Find Minimum in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''


class Solution(object):
    def findMin_niave(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in xrange(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        else:
            return nums[0]

    #  http://www.cnblogs.com/anne-vista/p/4899735.html
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (left + mid) / 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
