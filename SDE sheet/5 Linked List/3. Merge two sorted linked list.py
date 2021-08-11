"""
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def solve(a,b):
        if a == None:
            return b
        if b == None:
            return a
        result = None
        if a.val < b.val:
            result = a
            result.next = solve(a.next,b)
        else:
            result = b
            result.next = solve(a,b.next)
        return result
    return solve(l1,l2)