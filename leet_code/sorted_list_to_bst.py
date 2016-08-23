'''
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''
from data_structure.tree_node import TreeNode
from utilities.data_generator import *


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        node, length = head, 0
        while node:
            node = node.next
            length += 1
        self.curr = head
        return self._sortedListToBST(0, length - 1)

    def _sortedListToBST(self, left, right):
        if left > right:
            return None
        mid = (left + right) / 2
        left = self._sortedListToBST(left, mid - 1)
        root = TreeNode(self.curr.val)
        root.left = left
        self.curr = self.curr.next
        root.right = self._sortedListToBST(mid + 1, right)
        return root

    def sortedListToBST_2(self, head):
        if head is None:
            return None

        fast = head
        slow = head
        last_of_left = None
        while fast.next and fast.next.next:
            fast = fast.next.next
            last_of_left = slow
            slow = slow.next

        root = TreeNode(slow.val)

        if last_of_left:
            last_of_left.next = None
            root.left = self.sortedListToBST_2(head)

        if slow.next:
            root.right = self.sortedListToBST_2(slow.next)
        return root

s = Solution()
head = generate_list([1, 2, 3])
tree = s.sortedListToBST(head)
