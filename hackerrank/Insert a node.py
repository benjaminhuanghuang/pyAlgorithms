'''
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list?h_r=next-challenge&h_v=zen

'''


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def InsertNth(head, data, position):
    dummy = Node(-1)
    dummy.next = head
    curr = dummy
    i = 0
    while i < position and curr.next:
        curr = curr.next
        i += 1

    if curr.next:
        tmp = curr.next
        curr.next = Node(data)
        curr.next.next = tmp
    else:
        curr.next = Node(data)
    return dummy.next


h = InsertNth(None, 3, 0)
h = InsertNth(h, 5, 1)
h = InsertNth(h, 4, 2)
h = InsertNth(h, 2, 3)
h = InsertNth(h, 10, 1)

while h:
    print h.data
    h = h.next
