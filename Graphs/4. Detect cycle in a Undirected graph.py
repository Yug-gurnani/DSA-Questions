def cycle(graph,vis,parent,node):
    vis.append(node)
    for i in graph[node]:
        if i not in vis:
            if cycle(graph,vis,node,i):
                return True
        else:
            if parent != i:
                return True
    return False
