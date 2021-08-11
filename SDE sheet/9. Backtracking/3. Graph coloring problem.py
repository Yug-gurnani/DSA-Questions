"""
Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

Example 1:

Input:
N = 4
M = 3
E = 5
Edges[] = {(1,2),(2,3),(3,4),(4,1),(1,3)}
Output: 1
Explanation: It is possible to colour the
given graph using 3 colours.

The idea is to assign colors one by one to different vertices, starting from the vertex 0.
Before assigning a color, we check for safety by considering already assigned colors to the adjacent vertices.
If we find a color assignment which is safe,
we mark the color assignment as part of a solution.
If we do not a find color due to clashes then we backtrack and return false.
"""
def issafe(graph,V,v,color,c):
    for i in range(V):
        if graph[V][i] == 1 and color[i] == c:
            return False
    return True
            
def solve(graph,V,m,color,v):
    if v == V:
        return True
    for c in range(1,m+1):
        if issafe(graph,V,c,color,c):
            color[v] = c
            if solve(graph,V,m,color,v+1):
                return True
            color[v] = 0
    
        
def graphColoring(graph, k, V):
    '''
    :param graph: grid of size V*V in specified format(0 based indexing i.e. vertex 1 is index 0)
    :param k: number of colors allowed
    :param V: number of vertices 
    :return: True or False
    '''
    #your code here
    color = [0]*V
    if solve(graph,V-1,k,color,0) == True:
        return True
    return False
"""
TC = o(m^n)
SC = o(n)
"""