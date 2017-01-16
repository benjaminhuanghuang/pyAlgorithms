'''
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node
in the list or null.

Return a deep copy of the list.
'''


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    # http://www.kancloud.cn/kancloud/data-structure-and-algorithm-notes/73016
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head == None:
            return None

        myMap = {}
        new_head = RandomListNode(head.label)
        myMap[head] = new_head
        node_old = head
        node_new = new_head

        while node_old != None:
            node_new.random = node_old.random
            if node_old.next != None:
                node_new.next = RandomListNode(node_old.next.label)
                myMap[node_old.next] = node_new.next
            else:
                node_new.next = None
            node_old = node_old.next
            node_new = node_new.next

        p = new_head
        while p != None:
            if p.random != None:
                p.random = myMap[p.random]
            p = p.next
        return new_head
