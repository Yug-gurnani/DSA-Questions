"""
Given a Binary Tree with all unique values and two nodes value n1 and n2.
The task is to find the lowest common ancestor of the given two nodes.
We may assume that either both n1 and n2 are present in the tree or none of them is present. 

Example 1:

Input:
n1 = 2 , n2 =  3

     1
   /  \
  2    3
Output: 1

Example 2:

Input:
n1 = 3 , n2 = 4

         5
        /
       2
     /  \
    3    4
Output: 2

The idea is to traverse the tree starting from the root. If any of the given keys (n1 and n2) matches with the root,
then the root is LCA (assuming that both keys are present). If the root doesn’t match with any of the keys,
we recur for the left and right subtree. The node which has one key present in its left subtree and the other key present in the right subtree is the LCA.
If both keys lie in the left subtree, then the left subtree has LCA also, otherwise, LCA lies in the right subtree
"""
# This function returns pointer to LCA of two given
# values n1 and n2
# This function assumes that n1 and n2 are present in
# Binary Tree
def findLCA(root, n1, n2):
     
    # Base Case
    if root is None:
        return None
 
    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.key == n1 or root.key == n2:
        return root 
 
    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2) 
    right_lca = findLCA(root.right, n1, n2)
 
    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root 
 
    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca

"""
TC = o(n)
SC = o(n)
"""
