def dfs(graph,vis,i):
    vis.append(i)
    print(i)
    for j in graph[i]:
        if j not in vis:
            dfs(graph,vis,j)