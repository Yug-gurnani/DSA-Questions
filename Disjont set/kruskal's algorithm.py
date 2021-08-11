rank = [0] * (10**5+1)
parent = [i for i in range(10**5+1)]

def makeset():
    for i in range(len(rank)):
        rank[i] = 0
        parent[i] = i
def findPar(node):
    if node == parent[node]:
        return node
    parent[node] = findPar(parent[node])
    return parent[node]
def union(u,v):
    u = findPar(u)
    v = findPar(v)
    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[v] < rank[u]:
        parent[v] = u
    else:
        parent[v] = u
        rank[u] += 1

def main():
    makeset()
    n,m = map(int,input().split())

    edges = []
    for i in range(m):
        u,v,wt = map(int,input().split())
        edges.append([wt,u,v])

    edges.sort()
    cost = 0
    mst = []

    for i in edges:
        wt,u,v = i
        if findPar(u) != findPar(v):
            cost += wt
            mst.append([u,v,wt])
            union(u,v)

    print(cost)

    for i in mst:
        print("{} -- {} = {}".format(i[0],i[1],i[2]))

main()