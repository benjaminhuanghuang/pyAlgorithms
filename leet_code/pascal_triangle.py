'''
118. Pascal's Triangle
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            curr_row = []
            for j in range(i + 1):
                curr_row.append(1)
            if i > 1:
                for x in range(i - 1):
                    curr_row[x + 1] = result[i - 1][x] + result[i - 1][x + 1]
            print curr_row
            result.append(curr_row)
        return result


s = Solution()

s.generate(5)
