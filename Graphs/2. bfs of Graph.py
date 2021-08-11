def bfs(graph,start):
    visited = []
    queue = [start]
    visited.append(start)
    while queue:
        currnode = queue[0]
        print(currnode,end = " ")
        for i in graph[currnode]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    queue.pop(0)

