"""
Write a function to delete a node in a singly-linked list.
You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

 

Example 1:


Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

We simply swap the data of current node and next node till we reach the second last node and then remove it from the linked list.
"""
def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    while node.next.next:
        node.val,node.next.val = node.next.val,node.val
        node = node.next
    node.val,node.next.val = node.next.val,node.val
    node.next = None
    