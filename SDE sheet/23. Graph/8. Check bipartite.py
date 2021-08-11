"""
Given an adjacency list of a graph adj  of V no. of vertices having 0 based index. Check whether the graph is bipartite or not.
 

Example 1:

Input: 

Output: 1
Explanation: The given graph can be colored 
in two colors so, it is a bipartite graph.

Following is a simple algorithm to find out whether a given graph is Birpartite or not using Breadth First Search (BFS). 
1. Assign RED color to the source vertex (putting into set U). 
2. Color all the neighbors with BLUE color (putting into set V). 
3. Color all neighbor’s neighbor with RED color (putting into set U). 
4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2. 
5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot be colored with 2 vertices (or graph is not Bipartite) 
"""
def isBipartite(self, v, adj):
    def solve(v,adj,color,src):
        color[src] = 1
        q = [src]
        while q:
            curr = q[0]
            if curr in adj[curr]:
                return False
            for i in range(v):
                if i in adj[curr]:
                    if color[i] == -1:
                        color[i] = 1 - color[curr]
                        q.append(i)
                    elif color[i] == color[curr]:
                        return False
            q.pop(0)
        return True
    color = [-1] * v
    for i in range(v):
        if color[i] == -1:
            if not solve(v,adj,color,i):
                return False
    return True
"""
TC = o(V+E)
SC = o(V)
"""