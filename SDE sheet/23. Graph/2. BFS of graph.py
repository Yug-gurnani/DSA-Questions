"""
Do a breadth first search in a Graph
"""
from collections import deque
class Solution:
    def bfsOfGraph(self, V, adj):
        # code her
        ans = []
        q = deque([0])
        vis = {}
        while q:
            curr = q.popleft()
            vis[curr] = 1
            ans.append(curr)
            for i in adj[curr]:
                if i not in vis:
                    q.append(i)
        return ans
"""
TC = o(V+E)
SC = o(V)
"""