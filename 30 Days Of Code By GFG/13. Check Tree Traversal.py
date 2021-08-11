"""
Given Preorder, Inorder and Postorder traversals of some tree of size N.
The task is to check if they are all of the same tree or not.

Example 1:

Input:
N = 5
preorder[] = {1, 2, 4, 5, 3}
inorder[] = {4, 2, 5, 1, 3}
postorder[] = {4, 5, 2, 3, 1}
Output: Yes
Explanation: 
All of the above three traversals 
are of the same tree.
           1
         /   \
        2     3
      /   \
     4     5

Just derive the postorder from inorder and preorder and compare it to the given postorder
"""
import sys
sys.setrecursionlimit(10**9)
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def checktree(self, preorder, inorder, postorder, n): 
        # Your code goes here
        def postorde(root,arr):
            if not root:
                return
            postorde(root.left,arr)
            postorde(root.right,arr)
            arr.append(root.val)
        def solve(inn,pre,start,end,mp,preindex):
            if start > end:
                return
            curr = pre[preindex[0]]
            preindex[0] += 1
            tnode = Tree(curr)
            if start == end:
                return tnode
            inindex = mp[curr]
            tnode.left = solve(inn,pre,start,inindex-1,mp,preindex)
            tnode.right = solve(inn,pre,inindex+1,end,mp,preindex)
            
            return tnode
            
        if len(inorder) == len(preorder) == len(postorder):
            mp = {}
            for i in range(len(inorder)):
                mp[inorder[i]] = i
            preindex = [0]
            root = solve(inorder,preorder,0,n-1,mp,preindex)
            arr = []
            postorde(root,arr)
            #print(arr)
            return arr == postorder
        else:
            return False
"""
TC = o(n^2)
SC = o(n)
"""