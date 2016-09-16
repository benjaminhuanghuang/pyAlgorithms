'''
174. Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the
top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to
0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each
step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal
path RIGHT-> RIGHT -> DOWN -> DOWN.

'''


class Solution(object):
    # https://www.hrwhisper.me/leetcode-dynamic-programming/
    # dp[i][j] is the min health value can achieve [i,j]
    # min_hp_on_exit = min(dp[i+1][j],dp[i][j+1]), we will select the min one
    # dp[i][j]= max (0, min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j])
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for j in xrange(n)] for i in xrange(m)]
        dp[m - 1][n - 1] = max(0 - dungeon[m - 1][n - 1], 0)
        for i in xrange(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 0)
        for j in xrange(n - 2, -1, -1):
            dp[m - 1][j] = max(dp[m - 1][j + 1] - dungeon[m - 1][j], 0)
        for i in xrange(m - 2, -1, -1):
            for j in xrange(n - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 0)

        return dp[0][0] + 1

    # http://bookshadow.com/weblog/2015/01/07/leetcode-dungeon-game/
    #  min_HP_on_exit = min(dp[i+1][j], dp[i][j+1])
    #  if dungeon[i][j] == 0, dp[i][j] = min_HP_on_exit
    #  if dungeon[i][j] < 0,  dp[i][j] = min_HP_on_exit - dungeon[i][j]
    #  if dungeon[i][j] > 0,  dp[i][j] = max(min_HP_on_exit - dungeon[i][j],1)
    def calculateMinimumHP_11(self, dungeon):
        w = len(dungeon[0])
        h = len(dungeon)
        hp = [[0] * w for x in range(h)]

        hp[h - 1][w - 1] = max(0, -dungeon[h - 1][w - 1]) + 1

        for x in range(h - 1, -1, -1):
            for y in range(w - 1, -1, -1):
                down = None
                if x + 1 < h:
                    down = max(1, hp[x + 1][y] - dungeon[x][y])
                right = None
                if y + 1 < w:
                    right = max(1, hp[x][y + 1] - dungeon[x][y])
                if down and right:
                    hp[x][y] = min(down, right)
                elif down:
                    hp[x][y] = down
                elif right:
                    hp[x][y] = right
        return hp[0][0]