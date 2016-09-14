'''
375. Guess Number Higher or Lower II

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x.
You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n >= 1, find out how much money you need to have to guarantee a win.

Show Hint
http://bookshadow.com/weblog/2016/07/16/leetcode-guess-number-higher-or-lower-ii/
'''


class Solution(object):
    # if we guess x and x is a wrong answer, then we will guess in [1, x-1] or [x+1, n]
    # so, we need pay x + max(solve(1,x-1),solve(x+1,n))
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for i in range(n + 1)]
        return self.solve(dp, 1, n)

    def solve(self, dp, l, r):
        if l >= r:
            return 0
        if dp[l][r]:
            return dp[l][r]
        dp[l][r] = min(i + max(self.solve(dp, l, i - 1), self.solve(dp, i + 1, r)) for i in range(l, r + 1))
        return dp[l][r]
