"""
Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures.
It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]),
and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

This is BFS for traversing a Graph
"""
def bfsOfGraph(self, V, adj):
    vis = [False for i in range(V)]
    queue = [0]
    arr = [0]
    while queue:
        curr = queue[0]
        vis[curr] = True
        for i in adj[curr]:
            if not vis[i]:
                queue.append(i)
                vis[i] = True
                arr.append(i)
        queue.pop(0)
    return arr
"""
TC = o(V+E)
SC = o(V)
"""

"""
BFS for trees
"""
def bfsfortree(root):
    queue = [root]
    arr = [root.data]
    while queue:
        curr = queue[0]
        if curr.left:
            queue.append(curr.left)
            arr.append(curr.left.data)
        if curr.right:
            queue.append(curr.right)
            arr.append(curr.right.data)
        queue.pop(0)
    return arr