'''
354. Russian Doll Envelopes

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into
another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is
3 ([2,3] => [5,4] => [6,7]).


Reference:  Longest Increasing Subsequence

'''


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        # sort envelopes by width, if e1.width == e2.width, sort by height descending
        nums = sorted(envelopes, cmp=lambda e1, e2: e1[0] - e2[0] if e1[0] != e2[0] else e2[1] - e1[1])
        size = len(nums)
        dp = []
        for x in range(size):
            l, r = 0, len(dp) - 1
            while l <= r:
                mid = (l + r) / 2
                if dp[mid][1] < nums[x][1]:
                    l = mid + 1
                else:
                    r = mid - 1
            if l < len(dp):
                dp[l] = nums[x]
            else:
                dp.append(nums[x])
        return len(dp)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
s = Solution()
s.maxEnvelopes(envelopes)
