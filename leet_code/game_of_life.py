'''
289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised
by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its
eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
    Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells
first and then use their updated values to update other cells.

    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause
problems when the active area encroaches the border of the array. How would you address these problems?


http://my.oschina.net/Tsybius2014/blog/514447
'''


class Solution(object):
    # http://blog.csdn.net/xudli/article/details/48896549
    # dead-> live :0
    # dead-> dead :1
    # live-> live :10
    # live-> dead :11
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0 or board[0] is None or len(board[0]) == 0:
            return

        m = len(board)
        n = len(board[0])

        for i in xrange(m):
            for j in xrange(n):
                x = self.getLiveNun(board, i, j)
                if board[i][j] == 0:
                    if x == 3:
                        board[i][j] += 10
                else:
                    if x == 2 or x == 3:
                        board[i][j] += 10
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] /= 10

    def getLiveNun(self, board, x, y):
        c = 0
        for i in xrange(x - 1, x + 2):
            for j in xrange(y - 1, y + 2):
                if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i == x and j == y):
                    continue
                if board[i][j] % 10 == 1:
                    c += 1

        return c

    # http://bookshadow.com/weblog/2015/10/04/leetcode-game-life/
    def gameOfLife_2(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dx = (1, 1, 1, 0, 0, -1, -1, -1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for x in range(len(board)):
            for y in range(len(board[0])):
                lives = 0
                for z in range(8):
                    nx, ny = x + dx[z], y + dy[z]
                    lives += self.getCellStatus(board, nx, ny)
                if lives + board[x][y] == 3 or lives == 3:
                    board[x][y] |= 2

        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] >>= 1

    def getCellStatus(self, board, x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return 0
        return board[x][y] & 1


s = Solution()
board = [[1, 1], [1, 0]]
s.gameOfLife(board)
print board
