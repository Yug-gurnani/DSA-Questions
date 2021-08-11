"""
Given a BST and an integer. Find the least absolute difference between any node value of the BST and the given integer.

Example 1:

Input:
        10
      /   \
     2    11
   /  \ 
  1    5
      /  \
     3    6
      \
       4
K = 13
Output: 2
Explanation: K=13. The node that has
value nearest to K is 11. so the answer
is 2
"""
def minDiff(root, k):
    # code here
    floor = 0
    ceil = float('inf')
    def solve(root,k):
        nonlocal floor,ceil
        if not root:
            return
        if root.data == k:
            floor = k
            ceil = k
            return
        if root.data > k:
            if root.data < ceil:
                ceil = root.data
            solve(root.left,k)
        if root.data < k:
            if root.data > floor:
                floor = root.data
            solve(root.right,k)
    solve(root,k)
    return min(abs(ceil-k),abs(floor-k))
"""
TC = o(h)
SC = o(h)
"""