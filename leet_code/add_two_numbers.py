'''
2. Add Two Numbers

You are given two linked lists representing two non-negative numbers. The digits are stored
in reverse order and each of their nodes contain a single digit. Add the two numbers and
return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

'''

from data_structure.list_node import ListNode


class Solution(object):
    def addTwoNumbers_my(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        carry = 0
        while True:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            curr.val = sum % 10
            carry /= 10
            if l1 != None or l2 != None or carry != 0:
                # Good! add a new node to add wi
                curr.next = ListNode(0)
                curr = curr.next
            else:
                break
        return head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        carry = 0
        while True:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            curr.val = carry % 10
            carry /= 10
            if l1 != None or l2 != None or carry != 0:
                # Good! add a new node to add wi
                curr.next = ListNode(0)
                curr = curr.next
            else:
                break
        return head
