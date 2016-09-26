'''
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        self.dfs(root, result)
        return result[0]

    def dfs(self, root, result):
        if not root:
            return
        if root.left:
            if root.left.left or root.left.right:
                self.dfs(root.left, result)
            else:
                result[0] += root.left.val
        if root.right:
            self.dfs(root.right, result)

