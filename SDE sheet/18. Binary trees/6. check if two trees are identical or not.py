"""
Given two binary trees, the task is to find if both of them are identical or not. 

Example 1:

Input:
     1          1
   /   \      /   \
  2     3    2     3
Output: Yes
Explanation: There are two trees both
having 3 nodes and 2 edges, both trees
are identical having the root as 1,
left child of 1 is 2 and right child
of 1 is 3.
"""
def isIdentical(root1, root2):
    # Code here
    if not root1 and not root2:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.data != root2.data:
        return False
    return isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)
"""
TC = o(n)
SC = o(n)
"""