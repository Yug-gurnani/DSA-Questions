"""
Input:
       10
      /   \
     20   30
   /   \
  40   60
Output:
40 20 60 10 30 
30 10 60 20 40
Explanation:  DLL would be 
40<=>20<=>60<=>10<=>30.

Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place.
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL
The order of nodes in DLL must be same as Inorder of the given Binary Tree
The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

To avoid the use of extra space we have used prev a reference variable and just done the inorder traversal of the tree
"""
def bToDLL(root):
    # do Code here
    if not root:
        return
    prev = None
    head = None
    def solve(root):
        nonlocal prev,head
        if not root:
            return
        solve(root.left)
        if not prev:
            head = root
        else:
            root.left = prev
            prev.right = root
        prev = root
        solve(root.right)
    solve(root)
    return head