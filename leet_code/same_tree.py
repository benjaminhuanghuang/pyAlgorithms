'''
100. Same Tree
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''


def is_tree_same(t1, t2):
    if t1 is None and t2 is None:
        return True

    if t1 and t2 and t1.val == t2.val:
        return is_tree_same(t1.left, t2.left) and is_tree_same(t1.right, t2.right)

    return False

