"""
Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

A height balanced tree
        1
     /     \
   10      39
  /
5

An unbalanced tree
        1
     /    
   10   
  /
5
"""
def isBalanced(root):
    
    #add code here
    ans = [True]
    def height(root,ans):
        if not root:
            return 0
        
        lh = height(root.left,ans)
        rh = height(root.right,ans)
        #print(lh,rh)
        if abs(lh - rh) > 1:
            ans[0] = False
        
        
        return 1+max(lh,rh)
    height(root,ans)
    if not ans[0]:
        return 0
    return 1
            
"""
TC = o(n)
SC = o(n)
"""