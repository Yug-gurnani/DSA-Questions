"""
Given a binary tree and a leaf node called target.
Find the minimum time required to burn the complete binary tree
if the target is set on fire. It is known that in 1 second all 
nodes connected to a given node get burned.
That is, its left child, right child and parent.

Example 1:

Input :      
          1
        /   \
      2      3
    /  \      \
   4    5      6
       / \      \
      7   8      9
                   \
                   10

Target Node = 8
Output: 7
Explanation: If leaf with the value 
8 is set on fire. 
After 1 sec: 5 is set on fire.
After 2 sec: 2, 7 are set to fire.
After 3 sec: 4, 1 are set to fire.
After 4 sec: 3 is set to fire.
After 5 sec: 6 is set to fire.
After 6 sec: 9 is set to fire.
After 7 sec: 10 is set to fire.
It takes 7s to burn the complete tree.
"""

class Solution:
    def minTime(self, root,target):
        # code here
        ans = 0
        def solve(root):
            nonlocal target,ans
            if not root:
                return [0,0,False]
                
            left = solve(root.left)
            right = solve(root.right)
            
            
            if not root.left and not root.right:
                if root.data == target:
                    return [0,0,True]
            if left[2]:
                left[1] = 1 + left[1]
                ans = max(ans,left[1] + right[0])
            
            if right[2]:
                right[1] = 1+ right[1]
                ans = max(ans,right[1] + left[0])
                
            return [1+max(left[0],right[0]),max(left[1],right[1]),left[2] or right[2]]
        solve(root)
        return ans
"""
TC = o(n)
"""