'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


'''


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums or len(nums) <= 0:
            return []
        res = []
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                res.append(self.getString(start, end))
                start = nums[i]

            end = nums[i]

        # res.append(self.getString(start, end))

        return res

    def getString(self, start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + '->' + str(end)
