"""
slight variation of top view ,just continously change the dist of it and it will only take the dist visible from bottom
"""
def bottomView(root):
    from collections import deque,defaultdict
    dist = {root:0}
    dic = defaultdict()
    q = deque([root])
    ans = []
    while q:
        curr = q[0]
        currhd = dist[curr]
        
        dic[currhd] = curr.data
        if curr.left:
            dist[curr.left] = currhd-1
            q.append(curr.left)
        if curr.right:
            dist[curr.right] = currhd + 1
            q.append(curr.right)
        q.popleft()
    for i in sorted(dic):
        ans.append(dic[i])
    return ans
