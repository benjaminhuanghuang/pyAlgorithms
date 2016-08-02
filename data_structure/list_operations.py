from list_node import ListNode
from utilities.data_generator import *


def reverse_list_iterative(head):
    if head is None or head.next is None:
        return head

    prev = None

    while head:
        next = head.next;
        head.next = prev;
        prev = head
        head = next
    return prev


def reverse_list_recursive(head):
    if head is None or head.next is None:
        return head

    next = head.next
    head.next = None

    # next is the head before reverse and is the tail after reverse
    reversed = reverse_list_recursive(next)
    next.next = head
    return reversed


list = generate_list([1, 3, 5, 7, 8, 9])

list = reverse_list_iterative(list)

print_list(list)
