class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubTree(self, root1, root2):
        if root2 is None:  # no mater root1
            return True
        if root1 is None:
            return False

        if root1.val == root2.val:
            return self.isEqualTree(root1, root2)
        else:
            return self.isSubTree(root1.left, root2) or self.isSubTree(root1.right, root2)

    def isEqualTree(self, root1, root2):
        if root2 is None:  # no mater root1
            return True
        if root1 is None:
            return False

        if root1.val != root2.val:
            return False

        return self.isEqualTree(root1.left, root2.left) and self.isEqualTree(root1.right, root2.right)
