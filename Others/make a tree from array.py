import sys

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def build(arr,dic):
    #print(arr)
    if len(arr) == 0:
        return
    tmp = max(arr)
    root = Node(tmp)
    #print(root.val)
    idx = arr.index(tmp)
    root.left = build(arr[:idx],dic)
    root.right = build(arr[idx+1:],dic)
    return root
for _ in range(int(input())):
    n = int(input())
    arrr = list(map(int,input().split()))
    dic = {}
    root = build(arrr,dic)
    dic = {}
    q = [root]
    l = 0
    arr = [root.val]
    while q:
        curr = q[0]
        if len(q) == len(arr):
            for i in arr:
                dic[i] = l
            l += 1
            arr = []
        if curr.left:
            q.append(curr.left)
            arr.append(curr.left.val)
        if curr.right:
            q.append(curr.right)
            arr.append(curr.right.val)
        q.pop(0)
    for i in range(n):
        arrr[i] = dic[arrr[i]]
    print(*arrr)


            
    
    