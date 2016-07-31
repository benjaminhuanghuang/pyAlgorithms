'''

'''
import random

from data_structure.tree_node import TreeNode

def generate_random_list():
    random_items = [random.randint(-50, 100) for c in range(32)]
    return random_items


def genertate_bin_tree(nums):
    ""
    if not nums or len(nums) < 1:
        return None

    root = TreeNode()

    return root