# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:30:17 2020

@author: yuggu
"""


from collections import defaultdict

class Graph():
    def __init__(self):
        self.gph = defaultdict(list)
        self.next = None
    def addEdge(self,u,v,w=0):
        self.gph[u].append(v)
        
    def printGraph(self):
        graph = []
        for i in self.gph:
            for j in self.gph[i]:
                graph.append((i,j))
        return graph
    def printNeighbours(self,v):
        neig = []
        for i in self.gph[v]:
            neig.append(i)
        if neig:
            return neig
        else:
            return "No Padosi sed lyf"
    
    def BFS(self,s):
        visited = [False] * len(self.gph)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue[0]
            queue.pop(0)
            print(s,end = ' ')
            
            
            for i in self.gph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    
    def DFStraverse(self,v,visited):
        visited[v] = True
        print(v,end=' ')
        
        for i in self.gph[v]:
            if not visited[i]:
                self.DFStraverse(i,visited)
                
    def DFS(self,v):
        visited = [False]*(max(self.gph)+1)
        
        self.DFStraverse(v,visited)
        
            
        
        
        
        
        
    
myGraph = Graph()
myGraph.addEdge(0,1)
myGraph.addEdge(1,2)
myGraph.addEdge(0,2)
myGraph.addEdge(2,0)
myGraph.addEdge(2,3)
myGraph.addEdge(3,3)

print(myGraph.printGraph())
print(myGraph.printNeighbours(0))
myGraph.BFS(2)
print()
myGraph.DFS(0)