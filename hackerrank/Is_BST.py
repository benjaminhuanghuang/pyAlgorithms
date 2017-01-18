'''

'''

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


# Wrong!
def check_binary_search_tree_(root):
    if not root:
        return True
    if root.left:
        if root.left.data >= root.data:
            return False
    if root.right:
        if root.right.data <= root.data:
            return False

    return check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right)


MIN = 0
MAX = 10 ** 4


def check_binary_search_tree_(root):
    return check_BST(root, MIN, MAX)


def check_BST(root, min, max):
    if not root:
        return True

    if root.data <= min or root.data >= max:
        return False

    return check_BST(root.left, min, root.data) and check_BST(root.right, root.data, max)
