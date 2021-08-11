"""
Given below is a binary tree. The task is to print the top view of binary tree.
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Print from leftmost node to rightmost node.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3
"""
from collections import defaultdict,deque
def topView(root):
    '''
    :param root: root of the binary tree
    :return: None, newline is provided by driver code
    '''
    q = deque([root])
    dist = {root:0}
    dic = defaultdict()
    while q:
        curr = q[0]
        currdist = dist[curr]
        if currdist not in dic:
            dic[currdist] = curr.data
        if curr.left:
            dist[curr.left] = currdist - 1
            q.append(curr.left)
        if curr.right:
            dist[curr.right] = currdist + 1
            q.append(curr.right)
        q.popleft()
    ans =[]
    for i in sorted(dic):
        print(dic[i] , end = " ")
"""
TC = o(n)
SC = o(n)
"""