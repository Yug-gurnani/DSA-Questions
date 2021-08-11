"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
"""
from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        def find(graph,a,b,vis):
            q = [[a,1.0]]
            while q:
                curr = q.pop(0)
                
                if curr[0] == b:
                    return curr[1]
                for v in graph[curr[0]]:
                    if v[0] not in vis:
                        vis[v[0]] = True
                        q.append([v[0],v[1] * curr[1]])
            
        graph = defaultdict(list)
        dic = {}
        for i in range(len(equations)):
            a,b = equations[i][0],equations[i][1]
            val = values[i]
            graph[a].append([b,float(val)])
            graph[b].append([a,1/val])
        ans = []
        for i in queries:
            a,b = i[0],i[1]
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                
                tmp = find(graph,a,b,{})
                if tmp == None:
                    ans.append(-1.0)
                else:
                    ans.append(tmp)
        return ans