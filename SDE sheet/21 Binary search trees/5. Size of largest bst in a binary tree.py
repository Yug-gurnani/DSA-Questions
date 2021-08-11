"""
Given a binary tree. Find the size of its largest subtree that is a Binary Search Tree.

Example 1:

Input:
        1
      /   \
     4     4
   /   \
  6     8
Output: 1
Explanation: There's no sub-tree with size
greater than 1 which forms a BST. All the
leaf Nodes are the BSTs with size equal
to 1.

so to solve this in o(n) time we pass al list of size 3 in which we have:
1. True or False if the current subtree is bst or not
2. size of the Bst
3. min of that tree
4. Max of that tree

we identify is the subtree is bst or not by comparing the min and max node to root because in bst minnode < root < maxnode
so if it is true then it is a bst.
"""
def largestBst(root):
    #code here
    def solve(root):
        if not root:
            return [True,0,float('inf'),-float('inf')]
        if not root.left and not root.right:
            return [True,1,root.data,root.data]
        
        lbst = solve(root.left)
        rbst = solve(root.right)
        #print(lbst,rbst,root.data)
        ret = [0,0,0,0]
        if not lbst[0] or not rbst[0] or lbst[3] >= root.data or rbst[2] <= root.data:
            ret[0] = False
            ret[1] = max(lbst[1],rbst[1])
            return ret
        ret[0] = True
        ret[1] = 1 + lbst[1] + rbst[1]
        if not root.left:
            ret[2] = root.data
        else:
            ret[2] = lbst[2]
        if not root.right:
            ret[3] = root.data
        else:
            ret[3] = rbst[3]
        return ret
    ans = solve(root)
    return ans[1]
"""
TC = o(n)
SC = o(n)
"""