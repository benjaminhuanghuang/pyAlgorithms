'''
309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell
one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

'''


class Solution(object):
    # http://bookshadow.com/weblog/2015/11/24/leetcode-best-time-to-buy-and-sell-stock-with-cooldown/

    def maxProfit_1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if not size:
            return 0
        buys = [None] * size
        sells = [None] * size
        sells[0], buys[0] = 0, -prices[0]
        for x in range(1, size):
            delta = prices[x] - prices[x - 1]
            sells[x] = max(buys[x - 1] + prices[x], sells[x - 1] + delta)
            buys[x] = max(buys[x - 1] - delta, sells[x - 2] - prices[x] if x > 1 else None)

        return max(sells)

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
            """

        size = len(prices)
        if size < 2:
            return 0
        buys = [None] * size
        sells = [None] * size

        sells[0], sells[1] = 0, max(0, prices[1] - prices[0])
        buys[0], buys[1] = -prices[0], max(-prices[0], -prices[1])

        for x in range(2, size):
            sells[x] = max(sells[x - 1], buys[x - 1] + prices[x])
            buys[x] = max(buys[x - 1], sells[x - 2] - prices[x])
        return sells[-1]
