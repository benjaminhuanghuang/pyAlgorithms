'''
153. Find Minimum in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''


class Solution(object):
    # https://www.hrwhisper.me/leetcode-binary-search/
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums, left, right):
        if nums[left] <= nums[right]:  # [left....right] are ordered
            return nums[left]
        mid = (left + right) >> 1
        return min(self.search(nums, left, mid), self.search(nums, mid + 1, right))

    # if the mid is greater than low and high, mid is in front of pivot, search from mid to high;
    # otherwise, search from low to mid; Special case is the array is sorted(1, 2, 3, 4,...), and
    #  mid point to the first element of the array(1), so recursively find left part should include mid itself.
    def findMin_2(self, nums):
        low = 0
        high = len(nums) - 1

        while low <= high:
            if (low == high):
                return nums[low]
            mid = (high - low) / 2 + low
            if nums[mid] > nums[high]:  # mid located in left part (bigger part)
                low = mid + 1
            else:
                high = mid

        return nums[0]


nums = [3, 1, 2]

s = Solution()
print s.findMin(nums)
