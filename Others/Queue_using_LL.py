# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:24:29 2020

@author: sam
"""
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue():
    def __init__(self,size):
        self.size = size
        self.first = None
        self.last = None
        self.length = 0
        
    def enqueu(self,val):
        addnode = Node(val)
        if self.length == self.size:
            print('queue is full')
            return
        if self.last==None:
            self.first = addnode
            self.last = addnode
            self.length +=1            
            return
        else:
            self.first.next = addnode
            self.first = addnode
            self.length += 1
            
    def peek(self):
        print('the first element is: ',self.last.data,'\n')
        return
    
    def dequeue(self):
        if self.length==0:
            print('stack is empty')
            return
        else:
            d = self.last.next
            print('Deleted item is : ',self.last.data,'\n')
            del self.last
            self.last = d
            self.length -= 1
            return
    def traverse(self):
        temp = self.last
        while temp:
            print(temp.data)
            temp = temp.next
        
    
    
q = Queue(5)
q.enqueu(6)
q.enqueu(5)
q.enqueu(2)
q.enqueu(1019)

q.dequeue()
q.peek()
q.traverse()

        
