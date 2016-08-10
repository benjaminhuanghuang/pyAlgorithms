'''
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root]
        result = []
        while len(stack) > 0:
            result.append(stack[-1].val)
            new_level = []
            for item in stack:
                if item.left:
                    new_level.append(item.left)
                if item.right:
                    new_level.append(item.right)
            stack = new_level

        return result
