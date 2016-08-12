'''
86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
from data_structure.list_node import ListNode

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1 = ListNode(0)
        head2 = ListNode(0)
        p1 = head1
        p2 = head2

        current = head
        while current:
            if current.val < x:
                p1.next = current
                current = current.next
                p1 = p1.next
                p1.next = None
            else:
                p2.next = current
                current = current.next
                p2 = p2.next
                p2.next = None

        p1.next = head2.next
        head = head1.next
        return head