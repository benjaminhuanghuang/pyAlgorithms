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

http://www.jianshu.com/p/8f3b8df612ae
http://www.jiuzhang.com/solutions/n-queens/
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        if n <= 0:
            return result

        cols = []  # col nums of the queen's position in each row
        self.search(n, cols, result)
        return result

    def search(self, n, cols, result):
        if len(cols) == n:
            result.append(self.drawBoard(cols))
            return

        for col in range(n):
            if not self.isValid(cols, col):
                continue
            self.search(n, cols + [col], result)

    def isValid(self, cols, col):
        row_count = len(cols)
        for i in range(row_count):
            # same column
            if cols[i] == col:
                return False
            # left-top to right-bottom
            if i - cols[i] == row_count - col:
                return False
            # right-top to left-bottom
            if i + cols[i] == row_count + col:
                return False
        return True

    def drawBoard(self, cols):
        '''
        :param cols[i]: col num of queen's position in each row
        :return:
        '''
        board = []
        for i in range(len(cols)):
            line = ""
            for j in range(len(cols)):
                if j == cols[i]:
                    line += "Q"
                else:
                    line += "."
            board.append(line)
        return board


s = Solution()
print s.solveNQueens(5)
