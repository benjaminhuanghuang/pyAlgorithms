'''
220. Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the
difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.

'''

import collections


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False

        numDict = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1, t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[x] - numDict[m]) <= t:
                    return True
            numDict[key] = nums[x]
            if x >= k:
                numDict.popitem(last=False)
        return False

    # https://www.hrwhisper.me/leetcode-contains-duplicate-i-ii-iii/
    # put num to nums/(t+1) bucket
    def containsNearbyAlmostDuplicate_2(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        if t < 0:
            return False
        div = t + 1
        vis = {}
        for i, num in enumerate(nums):
            index = num / div
            if index in vis \
                    or index - 1 in vis and abs(vis[index - 1] - num) <= t \
                    or index + 1 in vis and abs(vis[index + 1] - num) <= t:
                return True
            vis[index] = num
            if i >= k:
                del vis[nums[i - k] / div]
        return False
