'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.


Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate
a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
http://www.jiuzhang.com/solutions/n-queens/
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

    def attack(self, row, col):
        for c, r in self.cols.it

        def dfs(depth, board, valuelist, solution):
            # for i in range(len(board)):
            if depth == len(board):
                solution.append(valuelist)
            for row in range(len(board)):
                if check(depth, row, board):
                    s = '.' * len(board)
                    board[depth] = row
                    dfs(depth + 1, board, valuelist + [s[:row] + 'Q' + s[row + 1:]], solution)

        board = [-1 for i in range(n)]
        solution = []
        dfs(0, board, [], solution)
        return solution
