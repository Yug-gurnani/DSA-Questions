"""
Given a binary tree. Check whether it is a BST or not.

Example 1:

Input:
    2
 /    \
1      3
Output: 1 
Explanation: 
The left subtree of root node contains node 
with key lesser than the root node’s key and 
the right subtree of root node contains node 
with key greater than the root node’s key.
Hence, the tree is a BST.

A simple approach to find out if the inorder of the tree is sorted and there are no duplicate elements
"""
def isBST(root):
    #code here
    def inorder(root,arr):
        if not root:
            return 
        if root.left:
            inorder(root.left,arr)
        arr.append(root.data)
        if root.right:
            inorder(root.right,arr)

    arr = []
    inorder(root,arr)
    return arr == sorted(list(set(arr)))
"""
TC = o(n)
SC = o(n)
"""
"""
To optimize space complexity we track of the prev node
"""
def isBSTUtil(root, prev): 
      
    # traverse the tree in inorder fashion  
    # and keep track of prev node 
    if (root != None): 
        if (isBSTUtil(root.left, prev) == True): 
            return False
  
        # Allows only distinct valued nodes  
        if (prev != None and
            root.data <= prev.data): 
            return False
  
        prev = root 
        return isBSTUtil(root.right, prev) 
      
    return True
  
def isBST(root): 
    prev = None
    return isBSTUtil(root, prev)
"""
TC = o(n)
SC = o(1)

"""
