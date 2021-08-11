"""
Given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use recursive approach to find the BFS traversal of the graph starting from the 0th vertex from left to right according to the graph..
"""
def dfsOfGraph(self, V, adj):
    # code here
    def dfs(i,adj,vis,ans):
        vis[i] = 1
        ans.append(i)
        for node in adj[i]:
            if node not in vis:
                dfs(node,adj,vis,ans)
    ans,vis = [],{}
    dfs(0,adj,vis,ans)
    return ans