#Any dfs will work
from collections import deque
from collections import defaultdict
def solve(root,d,dic):
    if not root:
        return
    dic[d].append(root.data)
    solve(root.left,d+1,dic)
    solve(root.right,d,dic)
def diagonal(root):
    if not root:
        return
    ans = []
    dic = defaultdict(list)
    solve(root,0,dic)
    for i in sorted(dic):
        for j in dic[i]:
            ans.append(j)
    return ans