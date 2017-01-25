'''
95. Unique Binary Search Trees II


Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


reference
    http://bangbingsyb.blogspot.com/2014/11/leetcode-unique-binary-search-trees-i-ii.html
'''

from data_structure.tree_node import TreeNode


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        return self.dfs(1, n)

    def dfs(self, start, end):
        if start > end:
            return [None]
        res = []
        for rootval in range(start, end + 1):
            LeftTree = self.dfs(start, rootval - 1)
            RightTree = self.dfs(rootval + 1, end)
            for ltree in LeftTree:
                for rtree in RightTree:
                    root = TreeNode(rootval)
                    root.left = ltree
                    root.right = rtree
                    res.append(root)
        return res


s = Solution()
res = s.generateTrees(3)
print res
