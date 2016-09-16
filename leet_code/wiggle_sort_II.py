'''
324. Wiggle Sort II

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

'''


class Solution(object):
    # time: O(NlogN) space O(N)
    # nums[1] > nums[0], nums[1] > nums[2]... means the number with odd index is bigger than previous and next one.
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        snums = sorted(nums)

        print range(1, size, 2) + range(0, size, 2)
        for x in range(1, size, 2) + range(0, size, 2):
            nums[x] = snums.pop()

    # time: O(N) space O(1)
    # https://discuss.leetcode.com/topic/32929/o-n-o-1-after-median-virtual-indexing
    def wiggleSort_2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        mid_index = n / 2
        mid = nums[mid_index]

        i = 0
        left = 0
        right = n - 1
        while (left <= right):
            if nums[left] > mid:
                pass
            elif nums[left] < mid:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1


nums = [1, 5, 1, 1, 6, 4]
s = Solution()
s.wiggleSort(nums)
print nums
