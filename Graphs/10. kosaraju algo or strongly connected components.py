"""
for printing SCCs
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
    print(node)
    for i in graph[node]:
        if not vis[i]:
            revdfs(i,graph,vis)
def solve(graph):
    vis = [False] * (len(graph)+1)
    stack = []
    for i in range(1,len(graph)+1):
        if not vis[i]:
            dfs(graph,i,stack,vis)
    graph = revgraph(graph)
    vis = [False] * (len(graph)+1)

    while stack:
        temp = stack.pop()
        if not vis[temp]:
            revdfs(temp,graph,vis)
    
