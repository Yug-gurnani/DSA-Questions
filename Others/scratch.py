# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:11:10 2020

@author: sam
"""


class MyArray:
    def __init__(self):
        self.data = {}
        self.length = 0
        
    def get(self, index):
        return self.data[index]
    
    def push(self, value):
        self.data[self.length] = value
        self.length += 1
        
    def pop(self):
        self.length -= 1
        temp = self.data[self.length]
        del self.data[self.length]
        return temp

    def delete(self, index):
        
        self.length -= 1
        while index != self.length:
            self.data[index] = self.data[index+1]
            index += 1
        del self.data[self.length]
        
        
array = MyArray()

array.push("lol")
array.push("ye kaydee sala")
var = array.pop()
array.push(69)
array.push("kamikaze")
array.push("kamikaze2")
array.delete(1)
array.push("lmfao")

print(array.data)