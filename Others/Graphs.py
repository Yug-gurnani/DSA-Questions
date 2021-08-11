# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:22:04 2020

@author: sam
"""
class Graph():
    def __init__(self):
        self.length = 0
        self.Graphdict = {}
        
    def adj(self,node):
        self.Graphdict[node] = []
        self.length +=1
        
        
    def addedge(self,node1,node2):
        self.Graphdict[node1].append(node2)
        self.Graphdict[node2].append(node1)
        
    def print_list(self):
        for i in self.Graphdict:
            print(i,'->',end=" ")
            for j in self.Graphdict[i]:
                
                print(j,end=' ')
            print('')
            
            
GG = Graph()
GG.adj('0')
GG.adj('1')
GG.adj('2')        
GG.adj('3')
GG.adj('4')
GG.adj('5')
GG.adj('6')

GG.addedge('3','1')
GG.addedge('3','4')
GG.addedge('4','2')
GG.addedge('4','5')
GG.addedge('1','2')
GG.addedge('1','0')
GG.addedge('0','2')
GG.addedge('6','5')
GG.print_list()
