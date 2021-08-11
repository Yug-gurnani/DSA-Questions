"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    slow = head
    fast = head
    for i in range(n):
        fast = fast.next
    prev = slow
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next
    if slow == head:
        return slow.next
    prev.next = slow.next
    return head
"""
TC = o(n)
SC = o(1)
"""