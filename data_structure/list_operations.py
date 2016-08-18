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


def insertionSortList(head):
    if not head:
        return head
    dummy = ListNode(0)
    dummy.next = head
    curr = head
    while curr.next:
        if curr.next.val < curr.val:
            pre = dummy
            while pre.next.val < curr.next.val:
                pre = pre.next
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        else:
            curr = curr.next
    return dummy.next


list = generate_list([1, 3, 5, 7, 8, 9])

list = reverse_list_iterative(list)

print_list(list)
