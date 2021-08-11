"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node,
just like in Figure B.
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

we will do bfs and for each level we run a loop and connect all the nodes without using extra space
"""

def connect(self, root: 'Node') -> 'Node':
    if not root:
        return None
    from collections import deque
    q = deque([root])

    while q:
        l = len(q)
        for i in range(l):
            temp = q.popleft()
            
            if i < l - 1:
                temp.next = q[0]
            else:
                temp.next = None
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
    return root
"""
TC = o(n)
SC = o(n) for q for bfsw
"""