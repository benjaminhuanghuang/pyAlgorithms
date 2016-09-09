'''
83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''


def delete_duplicates(head):
    if head == None:
        return None

    current = head
    while current.next:
        next = current.next
        if next.val == current.val:
            current.next = current.next.next
        else:
            current = next
    return head


