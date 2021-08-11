"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
def isPalindrome(self, head: ListNode) -> bool:
    if head == None or head.next == None:
        return True
    def rev(head):
        prev = None
        nex = None
        temp = head
        while temp:
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
        return prev
    slow = head
    fast = head
    while fast.next and fast.next.next:# Find the middle element of a linked list
        slow = slow.next
        fast = fast.next.next
    slow.next = rev(slow.next) #the reverse the other half of linked list
    slow = slow.next
    while slow:
        if head.val != slow.val:#then check is the first half and second reversed half is same or not
            return False
        slow = slow.next
        head = head.next
    return True