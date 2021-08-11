"""
it is only applicable in directed acyclic graphs
"""
def dfs(graph,node,vis,st):
    vis[node] = True
    for i in graph[node]:
        if not vis[i]:
            dfs(graph,i,vis,st)
    st.append(node)
def topological_sort(graph):
    st = []
    vis = [False] * len(graph)
    for node in graph:
        print(vis)
        if not vis[node]:
            dfs(graph,node,vis,st)
        
    print(*st[::-1])
graph = {5:[2,0],1:[],0:[],3:[1],2:[3],4:[0,1]}
topological_sort(graph)