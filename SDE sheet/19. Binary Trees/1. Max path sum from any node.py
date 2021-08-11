"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them
 A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
"""
def maxPathSum(self, root: TreeNode) -> int:
    def solve(root,res):
        if not root:
            return 0
        l = solve(root.left,res)
        r = solve(root.right,res)
        
        temp = max(max(l,r) + root.val,root.val)# to store if the left and right subtree is greater with root value or alone root value
        ans = max(temp,l+r+root.val) # to calculate if the subtree has the maximum sum or only one path from it has
        
        res[0] = max(res[0],ans) # to calculate final result
        return temp
    res = [-float('inf')]
    solve(root,res)
    return res[0]
"""
TC = o(n)
SC = o(n) for recursion
"""