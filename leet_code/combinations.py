'''
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.rec(res, 0, n, k, [])
        return res

    def rec(self, res, i, n, k, temp):
        if k == 0:
            res.append(temp)
            return
        for j in range(i + 1, n + 1):
            self.rec(res, j, n, k - 1, temp + [j])

    def combine_2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]

        out = []
        for i in range(1, n - k + 2):
            out.append([i])

        while True:
            node = out[0]
            if len(node) == k: break

            for j in range(node[-1] + 1, n + 1):
                out.append(node + [j])
            out.pop(0)

        return out
