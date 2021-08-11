"""
The cost of the spanning tree is the sum of the weights of all the edges in the tree.
There can be many spanning trees. Minimum spanning tree is the spanning tree where the cost is minimum among all the spanning trees.
There also can be many minimum spanning trees.

Minimum spanning tree has direct application in the design of networks.
It is used in algorithms approximating the travelling salesman problem, multi-terminal
minimum cut problem and minimum-cost weighted perfect matching. Other practical applications are:

Cluster Analysis
Handwriting recognition
Image segmentation



1) Create a set mstSet that keeps track of vertices already included in MST. 
2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE
Assign key value as 0 for the first vertex so that it is picked first. 
3) While mstSet doesn’t include all vertices 
….a) Pick a vertex u which is not there in mstSet and has minimum key value. 
….b) Include u to mstSet. 
….c) Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices. For every adjacent vertex v,
if weight of edge u-v is less than the previous key value of v, update the key value as weight of u-v
The idea of using key values is to pick the minimum weight edge from cut. The key values are used only for vertices which are not yet included in MST,
the key value for these vertices indicate the minimum weight edges connecting them to the set of vertices included in MST. 
"""
def minmst(mstset,key):
    minn = float('inf')
    minindex = None
    v = len(mstset)
    for i in range(v):
        if not mstset[i] and key[i] < minn:
            minn = key[i]
            minindex = i
    return minindex
def spanningTree( v, adj):
    mstset = [False] * v
    key = [float('inf')] * v
    key[0] = 0
    for i in range(v):
        u = minmst(mstset,key)
        mstset[u] = True
        for v in adj[u]:
            if mstset[v[0]] == False and v[1] < key[v[0]]:
                key[v[0]] = v[1]
    return sum(key)

