"""
YOu are given a binary tree and a target and a k number and you have to find the sum of all the nodes which are at 
<= k distance from the binary tree. including the target node
"""
from collections import deque
def store_parent(root,target,dic):
    if not root:
        return
    dic[root] = None
    ans = None
    q = deque([root])
    while q:
        curr = q[0]
        if curr.data == target:
            ans = curr
        if curr.left:
            dic[curr.left] = curr
            q.append(curr.left)
        if curr.right:
            dic[curr.right] = curr
            q.append(curr.right)
        q.popleft()

    return ans
def valentinesum(root,target,k):
    dic = {}
    t = store_parent(root,target,dic)
    if t == None or not root:
        return 
    check = {t:0}
    level = 0
    ans = 0
    q = deque([t])
    while q and level <= k:
        s = len(q)
        for i in range(s):
            curr = q[0]
            ans += curr.data
            if curr.left and curr.left not in check:
                q.append(curr.left)
                check[curr.left] = 1
            if curr.right and curr.right not in check:
                q.append(curr.right)
                check[curr.right] = 1
            if dic[curr] and dic[curr] not in check:
                q.append(dic[curr])
                check[dic[curr]] = 1
            q.popleft()
        level += 1
    return ans
"""
TC = o(n)
SC = o(n)
"""



    