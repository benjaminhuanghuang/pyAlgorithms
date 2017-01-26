'''
61. Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

'''
from data_structure.list_node import ListNode


class Solution(object):
    # can not pass [1, 2] 3
    # can not pass [1,2] 2
    def rotateRight_my(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k < 1:
            return head

        pfast = head
        pslow = head

        for i in xrange(k):
            if pfast.next:
                pfast = pfast.next
            else:
                # Wrong! Can not pass [1, 2] 3
                return head

        while pfast.next:
            pfast = pfast.next
            pslow = pslow.next

        new_head = pslow.next
        pslow.next = None
        pfast.next = head
        return new_head

    def rotateRight_cycle(self, head, k):
        if k == 0 or head is None:
            return head
        tail = head
        count = 1
        while tail.next:
            tail = tail.next
            count += 1
        # make a cycle
        tail.next = head
        step = count - (k % count)
        for i in xrange(step):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head





