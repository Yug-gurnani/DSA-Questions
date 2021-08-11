# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 23:49:25 2020

@author: Sam
"""

class Head_Tail():
    def _init_(self):
        self.head = None
        self.tail = None
    def traverse(self):
        #node = self.next
        
        temp = self.head
    
        while temp != None:
            print(temp.data,"--->",end=" ")
            temp = temp.next
            
        print("NULL")
        
    def reverse(self):
        a = self.head
        self.tail = self.head
        b = a.next 
        temp = b.next
        while temp:
            b.next = a
            a = b
            b = temp
            temp = temp.next
        b.next=a
        self.head.next = None
        self.head = b
        
        



class LinkedList():
    def __init__(self,data):
        self.data = data
        self.next = None
            
    
    def append(self,val):
        addNode = LinkedList(val)
        myLL.tail.next = addNode
        myLL.tail = addNode
        
    def prepend(self,val):
        addNode = LinkedList(val)
        addNode.next = myLL.head
        myLL.head = addNode
        
      
        
        
       
node = LinkedList(10)
myLL = Head_Tail()
myLL.head = node
myLL.tail = node
node.append(5)
node.append(6)
node.append(7)
node.prepend(1)
node.prepend(11)
node.append(69)
myLL.reverse()
myLL.traverse()


