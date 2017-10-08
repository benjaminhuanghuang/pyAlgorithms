def min_coins(coins, total):
    cols = total + 1
    rows = len(coins)
    dp = [[j if col == 0 else float("inf") for col in range(cols)] for j in range(rows)]

    for r in range(rows):
        for c in range(1, cols):
            if c < coins[r]:
                dp[r][c] = dp[r - 1][c]
            else:
                dp[r][c] = min(dp[r - 1][c], 1 + dp[r][c - coins[r]])

    return dp[rows - 1][cols - 1]




print min_coins([5,10,25], 30)