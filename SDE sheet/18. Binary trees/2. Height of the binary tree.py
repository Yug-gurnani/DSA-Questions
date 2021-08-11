"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
"""
def maxDepth(self, root: TreeNode) -> int:
    def solve(root):
        if not root:
            return 0
        return max(1 + solve(root.left),1+ solve(root.right))
    
    ans = solve(root)
    return ans
        