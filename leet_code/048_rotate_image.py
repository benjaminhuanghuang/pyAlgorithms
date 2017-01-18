'''
48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

Hints:
https://www.youtube.com/watch?v=flTKZiE25M8
'''


class Solution(object):
    # http://www.tianmaying.com/tutorial/LC48
    # [i, j] -> [j, n-i-1] -> [n-i-1, n-j-1] -> [n-j-1, i] -> [i, j]
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None:
            return

        n = len(matrix) - 1
        for i in xrange(n / 2 + 1):
            # xrange(i, n - i) for there are n is odd
            for j in xrange(i, n - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = tmp
