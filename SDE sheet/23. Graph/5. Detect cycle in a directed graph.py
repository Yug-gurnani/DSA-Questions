"""
Given a Directed Graph with V vertices and E edges, check whether it contains any cycle or not.


Example 1:

Input:



Output: 1
Explanation: 3 -> 3 is a cycle
"""
def isCyclic(self, v, adj):
    # code here
#    print(v)
    
    def dfs(adj,vis,rec,node):
        vis[node] = True
        rec[node] = True
        for i in adj[node]:
            if not vis[i] and dfs(adj,vis,rec,i):
                return True
            elif rec[i]:
                return True
        rec[node] = False
        return False
    rec = [False for i in range(v)]
    vis = [False for i in range(v)]
    for i in range(v):
        if not vis[i]:
            if dfs(adj,vis,rec,i):
                return True
    return False