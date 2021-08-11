"""
count the number of connected components in an undirected graph
"""
def dfs(graph,vis,node):
    vis[node] = True
    for i in graph[node]:
        if not vis[i]:
            dfs(graph,vis,i)

def cnt(graph):
    vis = [False] * (len(graph)+1)
    count = 0
    for i in range(len(graph)):
        if not vis[i]:
            dfs(graph,vis,node)
            count += 1
    return count
