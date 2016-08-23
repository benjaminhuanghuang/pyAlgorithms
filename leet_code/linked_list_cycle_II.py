'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

https://shenjie1993.gitbooks.io/leetcode-python/content/142%20Linked%20List%20Cycle%20II.html
'''


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                node = head
                while node != slow:
                    node = node.next
                    slow = slow.next
                return node
        return None
