from collections import defaultdict
def Topsort(g,vtx):
    indegree = [0]*vtx
    for i in range(vtx):
        for adjnode in g[i]:
            indegree[adjnode] += 1
    bfs = [x for x in range(vtx) if indegree[x]== 0]
    for node in bfs:
        for adjnode in graph[node]:
            indegree[adjnode] -= 1
            if indegree[adjnode] == 0:
                bfs.append(adjnode)
    return bfs

vtx,e = map(int,input().split())
graph = defaultdict(list)
for i in range(e):
    u,e = map(str,input().split())
    u = ord(u) - ord("A")
    e = ord(e) - ord("A")
    graph[u].append(e)
topsort = Topsort(graph,vtx)
print([chr(i+65) for i in topsort])
