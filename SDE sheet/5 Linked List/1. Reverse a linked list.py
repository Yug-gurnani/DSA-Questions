"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""
def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    nex = None
    temp = head
    while temp:
        nex = temp.next
        temp.next = prev
        prev = temp
        temp = nex
    head = prev
    return head
"""
TC = o(n)
SC = o(1)
"""
    