'''
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner
(row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which
contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12


Reference
    sums[i][j] = matrix[i-1][j-1] + sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1];
    result = sums[r2][c2] + sums[r1][c1] - sums[r2][c1] - sums[r1][c2];
'''


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.false_input = not matrix or not matrix[0]
        if self.false_input:
            return

        m, n = len(matrix) + 1, len(matrix[0]) + 1
        self.sum = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                self.sum[i][j] = self.sum[i][j - 1] + matrix[i - 1][j - 1]

        for i in xrange(1, m):
            for j in xrange(1, n):
                self.sum[i][j] = self.sum[i - 1][j] + self.sum[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.false_input:
            return 0
        return self.sum[row2 + 1][col2 + 1] - self.sum[row2 + 1][col1] - self.sum[row1][col2 + 1] \
               + self.sum[row1][col1]
