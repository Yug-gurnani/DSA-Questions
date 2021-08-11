"""
Disjoint set | union find by rank and path compression
"""
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
    m = int(input())
    while m:
        u,v = map(int,input().split())
        union(u,v)

        m -= 1
    # to check if 2 and 3 belongs to the same component
    print(parent[:7],rank[:7])
    if findPar(2) != findPar(3):
        print("DIFFERENT")
    else:
        print("SAME")
main()