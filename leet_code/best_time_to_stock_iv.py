'''
188. Best Time to Buy and Sell Stock IV

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''


class Solution(object):
    # https://www.hrwhisper.me/leetcode-best-time-to-buy-and-sell-stock-i-ii-iii-iv/
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if k >= size / 2:
            return self.quickSolve(size, prices)

        # dp[i][j] = trade[i] at day[j]
        # dp[i][j]=max(dp[i][j-1],prices[j] + maxTemp)
        dp = [[0 for j in xrange(size)] for i in xrange(k + 1)]

        for i in xrange(1, k + 1):
            maxTemp = -prices[0]
            for j in xrange(1, size):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxTemp)
                maxTemp = max(maxTemp, dp[i - 1][j - 1] - prices[j])
        return dp[k][size - 1]

    # refer to: Best Time to Buy and Sell Stock II
    def quickSolve(self, size, prices):
        sum = 0
        for x in range(size - 1):
            if prices[x + 1] > prices[x]:
                sum += prices[x + 1] - prices[x]
        return sum
