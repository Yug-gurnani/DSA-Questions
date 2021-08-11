"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list
and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Have to do this in O(1) space
"""
# Function to convert binary tree into
# linked list by altering the right node
# and making left node point to None
def flatten(root):
 
    # Base condition- return if root is None
    # or if it is a leaf node
    if (root == None or root.left == None and
                        root.right == None):
        return
     
    # If root.left exists then we have 
    # to make it root.right
    if (root.left != None):
 
        # Move left recursively
        flatten(root.left)
    
        # Store the node root.right
        tmpRight = root.right
        root.right = root.left
        root.left = None
 
        # Find the position to insert
        # the stored value   
        t = root.right
        while (t.right != None):
            t = t.right
 
        # Insert the stored value
        t.right = tmpRight
 
    # Now call the same function
    # for root.right
    flatten(root.right)
"""
TC = o(n)
SC = o(n)
"""