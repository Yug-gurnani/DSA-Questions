"""
A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.
 

Example 1:

Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity
approach :-
 
If A knows B, then A can't be a celebrity. Discard A, and B may be celebrity.
If A doesn't know B, then B can't be a celebrity. Discard B, and A may be celebrity.
Repeat above two steps till there is only one person.
"""

class Solution:
    def celebrity(self, mat, n):
        # code here 
        stack = []
        for i in range(n):
            stack.append(i)
        a = stack.pop()
        b = stack.pop()
        if n == 2:
            if mat[a][b] and not mat[b][a]:
                return b
            elif mat[b][a] and not mat[a][b]:
                return a
            return -1
                
        while len(stack) > 1:
            if mat[a][b]:
                a = stack.pop()
            else:
                b = stack.pop()
        
        if len(stack) == 0:
            return -1
        c = stack.pop()
        
        if mat[c][b]:
            c = b
        if mat[c][a]:
            c = a
        for i in range(n):
            if i != c and (mat[c][i] or (not mat[i][c])):
                return -1
        return c
"""
TC = o(n)
SC = o(n)
"""
