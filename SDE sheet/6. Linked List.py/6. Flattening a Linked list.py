"""
Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
Note: The flattened list will be printed using the bottom pointer instead of next pointer.

In this we use merge sort on linked list approach.
"""
def merge(a,b):# to merge two linked list
    if a == None:
        return b
    if b == None:
        return a
    result = None
    if a.data < b.data:
        result = a
        result.bottom = merge(a.bottom,b)
    else:
        result = b
        result.bottom = merge(a,b.bottom)
    return result
def flatten(root):
    #Your code here
    if not root:
        return None
    return merge(root,flatten(root.next))#to merge all the linked lists