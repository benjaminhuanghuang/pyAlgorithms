class Solution:
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node

        if root.val < node.val:
            root.right = self.insertNode(root.right, node)
        elif root.val > node.val:
            root.left = self.insertNode(root.left, node)
        return root
