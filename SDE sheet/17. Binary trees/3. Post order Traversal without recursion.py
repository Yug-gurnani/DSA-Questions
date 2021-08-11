"""
Postorder traversal is used to delete the tree. Please see the question for deletion of tree for details. Postorder traversal is also useful to get the postfix expression of an expression tree. Please see http://en.wikipedia.org/wiki/Reverse_Polish_notation to for the usage of postfix expression.

Example: Postorder traversal for the above given figure is 4 5 2 3 1.


Algorithm for Postorder without recursion

Following is the complete algorithm. After step 2, we get the reverse of a postorder traversal in the second stack. We use the first stack to get the correct order.

1. Push root to first stack.
2. Loop while first stack is not empty
   2.1 Pop a node from first stack and push it to second stack
   2.2 Push left and right children of the popped node to first stack
3. Print contents of second stack
"""
def postOrder(root):
    stack = [root]
    stack2 = []
    curr = root
    ans = []
    while stack:
        curr = stack.pop()
        stack2.append(curr.data)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return stack2[::-1]
"""
TC = o(n)
SC = o(n)
"""