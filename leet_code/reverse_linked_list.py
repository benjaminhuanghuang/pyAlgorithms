'''
206. Reverse Linked List


'''


def reverse_linked_list(head):
    prev = None
    current = head
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head
