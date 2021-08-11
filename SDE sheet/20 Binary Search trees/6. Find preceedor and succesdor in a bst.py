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
"""
def findPreSuc(root, key): 
  
    # Base Case 
    if root is None: 
        return
  
    # If key is present at root 
    if root.key == key: 
  
        # the maximum value in left subtree is predecessor 
        if root.left is not None: 
            tmp = root.left  
            while(tmp.right): 
                tmp = tmp.right  
            findPreSuc.pre = tmp 
  
  
        # the minimum value in right subtree is successor 
        if root.right is not None: 
            tmp = root.right 
            while(temp.left): 
                tmp = tmp.left  
            findPreSuc.suc = tmp  
  
        return 
  
    # If key is smaller than root's key, go to left subtree 
    if root.key > key : 
        findPreSuc.suc = root  
        findPreSuc(root.left, key) 
  
    else: # go to right subtree 
        findPreSuc.pre = root 
        findPreSuc(root.right, key)
"""
TC = o(n)
SC = o(1)
"""