"""
Given 2 Arrays of Inorder and preorder traversal. Construct a tree and print the Postorder traversal. 

Example 1:

Input:
N = 4
inorder[] = {1 6 8 7}
preorder[] = {1 6 7 8}
Output: 8 7 6 1

We can optimize the above solution using hashing (unordered_map in C++ or HashMap in Java).
We store indexes of inorder traversal in a hash table. So that search can be done O(1) time. 
"""

# Recursive function to construct binary of size
# len from Inorder traversal in[] and Preorder traversal
# pre[]. Initial values of inStrt and inEnd should be
# 0 and len -1. The function doesn't do any error
# checking for cases where inorder and preorder
# do not form a tree 
def buildTree(inn, pre, inStrt, inEnd):
     
    global preIndex, mp
 
    if (inStrt > inEnd):
        return None
 
    # Pick current node from Preorder traversal
    # using preIndex and increment preIndex 
    curr = pre[preIndex]
    preIndex += 1
    tNode = Node(curr)
 
    # If this node has no children then return 
    if (inStrt == inEnd):
        return tNode
 
    # Else find the index of this 
    # node in Inorder traversal 
    inIndex = mp[curr]
 
    # Using index in Inorder traversal, 
    # construct left and right subtress 
    tNode.left = buildTree(inn, pre, inStrt,
                           inIndex - 1)
    tNode.right = buildTree(inn, pre, inIndex + 1,
                            inEnd)
 
    return tNode
 
# This function mainly creates an 
# unordered_map, then calls buildTree()
def buldTreeWrap(inn, pre, lenn):
     
    global mp
     
    # Store indexes of all items so that we
    # we can quickly find later
    # unordered_map<char, int> mp;
    for i in range(lenn):
        mp[inn[i]] = i
 
    return buildTree(inn, pre, 0, lenn - 1)
"""
TC = o(n)
SC = o(n)
"""