"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Remember the edge cases,in case carry is remaining add the carry to the remaining node.
"""
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    def length(l):
        a = 0
        temp = l
        while temp:
            a += 1
            temp = temp.next
        return a
    
    a1 = length(l1)
    a2 = length(l2)
    if a1 >= a2:
        carry = 0
        t1 = l1
        t2 = l2
        while t1 and t2:
            temp = t1.val + t2.val + carry
            t1.val = temp%10
            carry = temp//10
            t1 = t1.next
            t2 = t2.next
        while t1:
            temp = t1.val + carry
            t1.val = temp%10
            carry = temp//10
            t1 = t1.next
        if carry:
            temp = l1
            while temp.next:
                temp = temp.next
            temp.next = ListNode(carry,None)
        return l1
    else:
        carry = 0
        t1 = l1
        t2 = l2
        while t1 and t2:
            temp = t1.val + t2.val + carry
            t2.val = temp%10
            carry = temp//10
            t1 = t1.next
            t2 = t2.next
        while t2:
            temp = t2.val + carry
            t2.val = temp%10
            carry = temp//10
            t2 = t2.next
        if carry:
            temp = l2
            while temp.next:
                temp = temp.next
            temp.next = ListNode(carry,None)
        return l2
"""
TC = o(n)
SC = o(1)

"""