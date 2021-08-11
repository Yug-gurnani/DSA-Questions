"""
Topological sort cannot be be done if the graph is not DAG directed acyclic graph

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

For example, a topological sorting of the following graph is “5 4 2 3 1 0”. There can be more than one topological sorting for a graph. For example, another topological sorting of the following graph is “4 5 2 3 1 0”. The first vertex in topological sorting is always a vertex with in-degree as 0 (a vertex with no incoming edges).
 
"""
def solve(vis,adj,node,stack):
    vis[node] = True
    for i in adj[node]:
        if not vis[i]:
            solve(vis,adj,i,stack)
    stack.append(node)
    
def topo(v,adj):
    vis = [False for i in range(v)]
    stack = []
    for i in range(v):
        if not vis[i]:
            solve(vis,adj,i,stack)
    return stack[::-1]

