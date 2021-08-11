"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

First make it a circular linked list and then break the connection after n - k +1 nodes and return the n - k + 1th node
"""
def rotateRight(self, head: ListNode, k: int) -> ListNode:
    l = 1
    if head == None:
        return None
    temp = head
    while temp.next:
        temp = temp.next
        l += 1
    
    if k > l:
        k = k%l
    elif k == l:
        return head
    temp.next = head
    t = l - k
    temp = head
    while temp and t > 1:
        temp = temp.next
        t -= 1
    ans = temp.next
    temp.next = None
    return ans