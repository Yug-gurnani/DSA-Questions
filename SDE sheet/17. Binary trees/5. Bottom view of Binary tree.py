"""
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
If there are multiple bottom-most nodes for a horizontal distance from root,
then print the later one in level traversal. For example, in the below diagram,
3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree the output should be 5 10 4 14 25.
 

Example 1:

Input:
       1
     /   \
    3     2
Output: 3 1 2
Explanation:
First case represents a tree with 3 nodes
and 2 edges where root is 1, left child of
1 is 3 and right child of 1 is 2.
"""
from collections import defaultdict,deque
def bottomView(root):
    dist = {root:0}
    q = deque([root])
    dic = defaultdict()
    while q:
        curr = q[0]
        currdist = dist[curr]
        dic[currdist] = curr.data
        if curr.left:
            dist[curr.left] = currdist - 1
            q.append(curr.left)
        if curr.right:
            dist[curr.right] = currdist + 1
            q.append(curr.right)
        q.popleft()
    ans = []
    for i in sorted(dic):
        ans.append(dic[i])
    return ans
"""
TC = o(n)
SC = o(n)
"""