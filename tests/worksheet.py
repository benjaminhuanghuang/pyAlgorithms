def maxProfit(prices):
    if not prices or len(prices) < 0:
        return 0

    minPrice = prices[0]
    hPrice = 0
    lPrice = 0
    profit = prices[1] - prices[0]
    for i in xrange(1, len(prices)):
        minPrice = min(minPrice, prices[i])
        if (prices[i] - minPrice > profit):
            profit = max(profit, prices[i] - minPrice)
            hPrice = prices[i]
            lPrice = minPrice
    if profit < 0:
        return 0, lPrice, hPrice
    return profit, lPrice, hPrice

list = [10, 1, 15]

p , l, h = maxProfit(list)
print "the profit is {0}, lowest price is {1}, highest price is {2}".format(p, l, h)