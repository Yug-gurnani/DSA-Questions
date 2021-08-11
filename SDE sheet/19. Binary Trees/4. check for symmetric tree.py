"""
Given a Binary Tree. Check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself or not.

Example 1:

Input:
         5
       /   \
      1     1
     /       \
    2         2
Output: True
Explanation: Tree is mirror image of
itself i.e. tree is symmetric

The idea is to write a recursive function isMirror() that takes two trees as an argument and returns true if trees are the mirror and false if trees are not mirror.
The isMirror() function recursively checks two roots and subtrees under the root.
"""
def isSymmetric(root):
    # Your Code Here
    if not root:
        return True
    ans = True
    def solve(root1,root2):
        if not root1 and not root2:
            return True
        if root1 and root2:
            if root1.data == root2.data:
                return solve(root1.left,root2.right) and solve(root1.right,root2.left)
        return False
    return solve(root,root)
"""
TC = o(n)
SC = o(n)
"""