# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:09:42 2020

@author: yuggu
"""
def printsolution(solution,n):
    for i in range(n):
        print()
        for j in range(n):
            print(solution[i][j],end=' ')
    print('\n')
    #return arr
def backtrack(arr,solution,x,y,n):
    if x == n-1 and y == n-1:
        printsolution(solution,n)
        solution[x][y]=1
        return
    if x < 0 or y<0 or x >= n or y >= n or arr[x][y] == 0 or solution[x][y]==1:
        return
    solution[x][y] = 1
    backtrack(arr,solution,x+1,y,n)
    backtrack(arr,solution,x-1,y,n)
    backtrack(arr,solution,x,y+1,n)
    backtrack(arr,solution,x,y-1,n)
    solution[x][y] = 0
def findPath(arr, n):
    solution = [[0 for i in range(n)]for j in range(n)]
    backtrack(arr,solution,0,0,n)

arr = [[1 for x in range(3)]for y in range(3)]
arr[0][2] = 0 
 
findPath(arr,3)