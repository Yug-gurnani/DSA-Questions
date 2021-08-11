"""
A directed graph is strongly connected if there is a path between all pairs of vertices.
A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph. For example, there are 3 SCCs in the following graph.
"""
from collections import defaultdict
def dfs(graph,node,stack,vis):
    vis[node] = True
    for i in graph[node]:
        if not vis[i]:
            dfs(graph,i,stack,vis)
    stack.append(node)
def revgraph(graph):
    new = defaultdict(list)
    for i in range(1,len(graph)+1):
        for node in graph[i]:
            new[node].append(i)
    return new
def revdfs(node,graph,vis):
    vis[node] = True
    for i in graph[node]:
        if not vis[i]:
            revdfs(i,graph,vis)
def countSCCs(graph, v):
    vis = [False] * (v)
    stack = []
    for i in range(v):
        if not vis[i]:
            dfs(graph,i,stack,vis)
    graph = revgraph(graph)
    vis = [False] * (v)
    count = 0
    while stack:
        temp = stack.pop()
        if not vis[temp]:
            count += 1
            revdfs(temp,graph,vis)
    return count
"""
TC = o(V+E)
SC = o(v)
"""