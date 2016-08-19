'''
279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''

import sys

import math


class Solution(object):
    # if x = a + b*b,
    # Time limit exceeded
    def numSquares_tle(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [sys.maxint] * (n + 1)
        i = 0
        while i <= math.sqrt(n):
            dp[i * i] = 1
            i += 1

        for i in xrange(n + 1):
            j = 0
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])
                j += 1
        return dp[n]
    # TLE
    def numSquares_tle2(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [sys.maxint] * (n + 1)
        dp[0] = 0
        for i in xrange(n + 1):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])
                j += 1
        return dp[n]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [0]
        while len(l) <= n:
            l += min(l[-i * i] for i in range(1, int(len(l) ** 0.5 + 1))) + 1,
        return l[n]



s = Solution()
print s.numSquares(12)
