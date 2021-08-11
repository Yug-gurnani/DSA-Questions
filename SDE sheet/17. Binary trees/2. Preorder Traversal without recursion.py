"""
Uses of Preorder
Preorder traversal is used to create a copy of the tree. Preorder traversal is also used to get prefix expression on of an expression tree.
Please see http://en.wikipedia.org/wiki/Polish_notation to know why prefix expressions are useful.
Example: Preorder traversal for the above given figure is 1 2 4 5 3.

Algorithm for preorder Traversal without recursion

1) Create an empty stack nodeStack and push root node to stack. 
2) Do following while nodeStack is not empty. 
….a) Pop an item from stack and print it. 
….b) Push right child of popped item to stack 
….c) Push left child of popped item to stack
Right child is pushed before left child to make sure that left subtree is processed first.
"""
def preorder(root):
    stack = [root]
    ans = []
    curr = root
    while True:
        if stack:
            curr = stack.pop()
            ans.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        else:
            break
    return ans
"""
TC = o(n)
SC = o(n)
"""