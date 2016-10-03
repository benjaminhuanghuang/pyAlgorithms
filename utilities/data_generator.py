'''

'''
import random

from data_structure.tree_node import TreeNode
from data_structure.list_node import ListNode

def generate_random_list():
    random_items = [random.randint(-50, 100) for c in range(32)]
    return random_items


def genertate_bin_tree(nums):
    ""
    if not nums or len(nums) < 1:
        return None

    root = TreeNode()

    return root

def generate_list(nums):
    head = ListNode(0)
    curr = head
    for i in xrange(1,len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next

    return head.next


def print_list(head):
    while head:
        print head.val
        head = head.next
    print " "