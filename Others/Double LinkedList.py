# -- coding: utf-8 --
"""
Created on Fri Jun 26 21:13:56 2020

@author: sam
"""

class Head_Tail():
    def __init__(self):
        self.head = None
        self.tail = None
       
    def traverse(self):
        
        
        #node = self.next
        
        temp = self.head
    
        while temp != None:
            print(temp.data,"--->",end=" ")
            
            temp = temp.next
            
        print("NULL")
        
    
    
    def getlis(self):
        self.lis = []
        
        #node = self.next
        
        temp = self.head
    
        while temp != None:
            
            self.lis.append(temp.data)
            temp = temp.next
            
       
        
   
    
    def rev_traverse(self):
        rlis = []
        #node = self.next
        
        temp = self.tail
    
        while temp != None:
            print(temp.data,"--->",end=" ")
            rlis.append(temp.data)
            temp = temp.prev
            
        print("NULL")
        return rlis



class LinkedList():
    def __init__(self,data):
        
            self.data = data
            self.next = None
            self.prev = None
            self.length = 1
            
    
    def append(self,val):
        addNode = LinkedList(val)
        myLL.tail.next = addNode
        addNode.prev = myLL.tail
        myLL.tail = addNode
        #print(addNode.prev.data)
        #print(myLL.head.prev)
       
        
        
        
    def prepend(self,val):
        addNode = LinkedList(val)
        addNode.next = myLL.head
        myLL.head.prev = addNode
        #print(myLL.head.prev.data)
        myLL.head = addNode
        
        
    def insert(self,index,val):
        myLL.getlis()
        addnode = LinkedList(val)
        if index == len(myLL.lis)-1:
            self.append(val)
            return    
        elif index == 0 :
            self.prepend(val)
            return
        
       
        if len(myLL.lis)/2 >= index:
            if index == 0:
                self.prepend(val)
                return
            a = myLL.head
            for i in range(index-1):
                a = a.next
            b = a.next
            a.next = addnode
            addnode.next = b
            b.prev = addnode
            addnode.prev = a
        else:
            a = myLL.tail
            for i in range(len(myLL.lis)-index-1):
                a = a.prev
            b = a.prev
            a.prev = addnode
            addnode.prev = b
            addnode.next = a
            b.next = addnode
            
            
                
            
    
    
    
    def remove(self,index):
        #a = myLL.head
        myLL.getlis()
        print(len(myLL.lis)/2,index)
        
        if index == len(myLL.lis)-1:
            a = myLL.tail
            b = a.prev
            myLL.tail = b
            b.next = None
            del a
            return
        
        elif index == 0 :
            a = myLL.head
            b = a.next
            myLL.head = b
            b.prev = None
            del a
            return
            
            
        
        if index <= len(myLL.lis)/2:
            a = myLL.head
            for i in range(index-1):
                a = a.next
            delete = a.next
            b = delete.next
            a.next = b
            b.prev = a
            del delete
        else:
            a = myLL.tail
            for i in range(len(myLL.lis)-index-2):
                print(len(myLL.lis))

                a = a.prev
                print(a.data)

            delete = a.prev
            b = delete.prev
            b.next = a
            a.prev = b
            
            del delete
            
            
                
        
      
        
        
       
node = LinkedList(10)
myLL = Head_Tail()
myLL.head = node
myLL.tail = node
node.append(5)
node.append(6)
node.append(7)

node.prepend(1)

node.append(69)

node.prepend(11)

node.insert(6,"g")
#node.remove(0)

myLL.traverse()
myLL.rev_traverse()