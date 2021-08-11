# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:40:34 2020

@author: yuggu
"""


class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class Tree():
    def __init__(self):
        self.root = None
        
    def insert(self,val):
        addnode = Node(val)
        if self.root == None:
            self.root = addnode
            return
        temp = self.root
        while temp:
            if temp.value == val:
                print('No Duplicate Allowed')
                return
            if val < temp.value:
                if temp.left == None:
                    temp.left = addnode
                    return
                temp = temp.left
            elif val > temp.value:
                if temp.right==None:
                    temp.right = addnode
                    return
                temp = temp.right
                
    def lookup(self,val):
        temp = self.root
        while temp:
            if temp.value == val:
                print(val,'found')
                return
                    
            if val < temp.value:
                temp = temp.left
                
            elif val > temp.value:
                temp = temp.right
          
        print(val,'value Not found')
        return
    
    def breadth_first_search(self):
        array = []
        queue = []
        currentnode = self.root
        queue.append(currentnode)
        
        while queue:
            currentnode = queue[0]
            if currentnode.left:
                queue.append(currentnode.left)
                
            if currentnode.right:
                queue.append(currentnode.right)
            array.append(currentnode.value)
            queue.pop(0)
                
        return array
    
    def DFSinorder(self):
        return TraverseinOrder(self.root,[])
    
    
    def DFSpreorder(self):
        return TraversepreOrder(self.root,[])

    def DFSpostorder(self):
        
        return TraversepostOrder(self.root,[])
    
    
    
def TraverseinOrder(root,dfs):
    if root.left:
        TraverseinOrder(root.left,dfs)
    dfs.append(root.value)
    if root.right:
        TraverseinOrder(root.right,dfs)
    print(dfs)
    return dfs

def TraversepreOrder(root,dfs):
    dfs.append(root.value)
    
    if root.left:
        TraversepreOrder(root.left,dfs)
    
    if root.right:
        TraversepreOrder(root.right,dfs)
    print(dfs)
    return dfs

def TraversepostOrder(root,dfs):
    if root.left:
        TraversepostOrder(root.left,dfs)
    
    if root.right:
        TraversepostOrder(root.right,dfs)
    dfs.append(root.value)
    print(dfs)
    return dfs
            
            
            
        
                    
            
                
t = Tree()
t.insert(9)
t.insert(6)
t.insert(12)
t.insert(1)
t.insert(8)
t.insert(10)
t.insert(14)
#t.breadth_first_search()
t.DFSinorder()
t.DFSpreorder()
t.DFSpostorder()