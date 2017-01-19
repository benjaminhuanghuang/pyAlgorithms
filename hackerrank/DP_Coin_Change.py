'''

DP: Coin Change



n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)


'''


def make_change(coins, amount):
    dp = [0 for i in range(amount + 1)]

    dp[0] = 1
    for c in coins:
        for i in range(c, amount + 1):
            dp[i] += dp[i - c]
    return dp[-1]


coins = [2, 5, 3, 6]
amount = 10

print make_change(coins, amount)
