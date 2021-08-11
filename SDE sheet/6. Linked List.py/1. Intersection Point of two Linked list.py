"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.


Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
"""
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    def length(node):
        l = 0
        temp = node
        while temp:
            l += 1
            temp = temp.next
        return l
    l1 = length(headA)
    l2 = length(headB)
    temp = headA
    temp2 = headB
    if l1 > l2:
        while l1 > l2 and temp:
            temp = temp.next
            l1 -= 1
    elif l2 > l1:
        while l2 > l1 and temp2:
            temp2 = temp2.next
            l2 -= 1
    ans = None
    while temp and temp2:
        if temp == temp2:
            ans = temp
            break
        temp = temp.next
        temp2 = temp2.next
    return ans
"""
TC = o(n+m)
SC = o(1)
"""