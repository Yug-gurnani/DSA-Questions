"""
always use level order traversal in view type questions
"""
from collections import deque
def topView(root):
    dist = {root:0}
    dic = {}
    q = deque([root])
    while q:
        curr = q[0]
        currhd = dist[curr]
        if currhd not in dic:
            dic[currhd] = curr.data
        if curr.left:
            dist[curr.left] = currhd-1
            q.append(curr.left)
        if curr.right:
            dist[curr.right] = currhd + 1
            q.append(curr.right)
        q.popleft()
    for i in sorted(dic):
        print(dic[i],end = " ")