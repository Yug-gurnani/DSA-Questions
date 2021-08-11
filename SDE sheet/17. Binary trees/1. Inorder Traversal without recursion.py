"""
Uses of Inorder
In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. 
To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal s reversed can be used.
Example: Inorder traversal for the above-given figure is 4 2 5 1 3.

Algorithm for inorder traversal without recursion

1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
"""
def InOrder(root):
    stack = []
    curr = root
    ans = []
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            ans.append(curr.data)
            curr = curr.right
        else:
            break
    return ans
"""
TC = o(n)
SC = o(n)
"""