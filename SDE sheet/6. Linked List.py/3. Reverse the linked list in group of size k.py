"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    l = 0
    temp = head
    while temp:
        temp = temp.next
        l += 1
    
    def solve(head,k,l):
        print(l)
        prev = None
        nex = None
        temp = head
        count = 0
        while temp and count < k:
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
            count += 1
            l -= 1
        if nex:
            if l < k:
                head.next = nex
            else:
                head.next = solve(nex,k,l)
        return prev
    return solve(head,k,l)
"""
TC = o(n)
SC = o(1)
"""