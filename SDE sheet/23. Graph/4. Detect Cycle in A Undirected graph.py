"""
Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. 

Example 1:

Input:   

Output: 1
Explanation: 1->2->3->4->1 is a cycle.
"""
def isCycle(self, V, adj):
		#Code here
    def solve(adj,vis,node,parent):
        vis[node] = True
        for i in adj[node]:
            if not vis[i]:
                if solve(adj,vis,i,node):
                    return True
            else:
                if parent != i:
                    return True
        return False
    vis = [False for i in range(V)]
    for i in range(V):
        if not vis[i]:
            if solve(adj,vis,i,-1):
                return True
    return False