'''
78. Subsets

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return [[]]
        nums.sort()

        result = []
        line = []
        self.helper(result, line, nums, 0)
        return result

    def helper(self, result, line, nums, k):
        result.append(list(line))    # append a copy of line to result

        for i in range(k, len(nums)):
            line.append(nums[i])
            self.helper(result, line, nums, i + 1)
            line.pop()


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        result = []
        line = []
        self.helper(nums, result, line)
        return result

    def helper(self, nums, result, line):
        result.append(list(line))    # append a copy of line to result

        for i, x in enumerate(nums):
            # in this loop, line + nums[i]...line + nums[n]
            line.append(x)
            self.helper(nums[i+1:], result, line)
            line.pop()


s = Solution()
print s.subsets([1,2,3])
