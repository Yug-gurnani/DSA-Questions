def dfs(graph,node,vis,rec):
    vis[node] = True
    rec[node] = True
    for i in graph[node]:
        if not vis[i] and dfs(graph,i,vis,rec):
            return True
        elif rec[i]:
            return True
    rec[node] = False
    return False
def cycle(graph):
    vis = [False]*len(graph)
    rec = [False]*len(graph)
    for i in range(1,len(graph)):
        if not vis[i]:
            if dfs(graph,i,vis,rec):
                return True
    return False
