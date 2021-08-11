"""
implementation of undirected graph
"""
from collections import defaultdict
graph = defaultdict(list)
u,v = map(int,input().split())
for i in range(v):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)