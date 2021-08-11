import heapq
from collections import defaultdict
def shortest_path(graph,src,dest):
    h = []
    flag = False
    heapq.heappush(h,(0,src))
    while len(h)>0:
        currcost,currver = heapq.heappop(h)
        if currver == dest:
            flag = True
            print("Path exist between {} and {} with cost {}".format(src,dest,currcost))
            break
        for neigh,neighcost in graph[currver]: 
            heapq.heappush(h,(currcost+neighcost,neigh))

    if not flag:
        print("No path found")

    
graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,s,c = map(str,input().split())
    graph[u].append([s,int(c)])
src,dest = map(str,input().split())
shortest_path(graph,src,dest)

"""
EXAMPLE TEST CASE
6 7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11 
E D 4 
A F
ANS:
Path exist between A and F with cost 20
"""

