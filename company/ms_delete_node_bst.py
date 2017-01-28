class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def DeleteNode(self, root, val):
        if not root:
            return root

        if root.val < val:
            root.right = self.DeleteNode(root.right, val)

        elif root.val > val:
            root.left = self.DeleteNode(root.left, val)
        else:  # root.val  == val
            if not root.left:
                return root.right
            else:
                pre = root.left
                while pre and pre.right:
                    pre = pre.right
                root.val = pre.val
                root.left = self.DeleteNode(root.left, val)
        return root
