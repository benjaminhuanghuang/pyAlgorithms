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
        return self._sortedListToBST(head, 0, length - 1)

    def _sortedListToBST(self, head, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        left = self._sortedListToBST(head, start, mid - 1)
        parent = TreeNode(head.val)
        parent.left = left
        head = head.next
        parent.right = self._sortedListToBST(head, mid + 1, end)
        return parent

    def sortedListToBST_2(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.cur = head
        node, length = head, 0
        while node:
            node = node.next
            length += 1
        return self.build_tree(length)

    def build_tree(self, n):
        if n <= 0:
            return None
        l = self.build_tree(n / 2)
        root = TreeNode(self.cur.val)
        self.cur = self.cur.next
        r = self.build_tree(n - n / 2 - 1)
        root.left = l
        root.right = r
        return root

    def sortedListToBST_3(self, head):
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
tree = s.sortedListToBST_2(head)
