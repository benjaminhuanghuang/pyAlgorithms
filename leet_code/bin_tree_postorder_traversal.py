'''
145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
'''


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3720846.html
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack = []

        pre = None
        if root:
            stack.append(root)
            while stack:
                curr = stack[-1]
                if (curr.left == None and curr.right == None) or (pre and (pre == curr.left or pre == curr.right)):
                    list.append(curr.val)
                    stack.pop()
                    pre = curr
                else:
                    if curr.right:
                        stack.append(curr.right)
                    if curr.left:
                        stack.append(curr.left)
        return list

    def recursive_postorder(self, root):
        if root is None:
            return []

        list = []
        if root:
            list += self.recursive_postorder(root.left)
            list += self.recursive_postorder(root.right)
            list.append(root.val)

        return list
