"""
Given inorder and postorder traversals of a Binary Tree in the arrays in[] and post[] respectively.
The task is to construct the binary tree from these traversals.
Input:
N = 8
in[] = 4 8 2 5 1 6 3 7
post[] =8 4 5 2 6 7 3 1
Output: 1 2 4 8 5 3 6 7
Explanation: For the given postorder and
inorder traversal of tree the  resultant
binary tree will be
           1
       /      \
     2         3
   /  \      /  \
  4    5    6    7
   \
     8
The idea is similiar to Inorder and preorder but we reverse the process as calling right subtree first cause in post order right subtree
is near to root
"""
def buildTree(In, post, n):
    
    # your code here
    
    '''
    :param In: given in order array
    :param post: given post order array
    :param n: number of nodes in tree
    :return: root of the created tree 
    '''
    dic = {}
    for i in range(n):
        dic[In[i]] = i
    ind = n-1
    def solve(In,post,start,end):
        nonlocal dic,ind
        if start > end:
            return None
        curr = post[ind]
        ind -= 1 # reverse indexing because postorder has root at the end
        tnode = Node(curr)
        if start == end:
            return tnode
        nextindex = dic[curr]
        tnode.right = solve(In,post,nextindex + 1,end)
        tnode.left = solve(In,post,start,nextindex-1)

        return tnode
    return solve(In,post,0,n-1)