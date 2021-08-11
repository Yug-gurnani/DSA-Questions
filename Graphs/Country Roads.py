"""
A country can be represented as a tree with n nodes and n - 1 edges. Each node represents a town, and each edge represents a piece of road.

You’re given two lists of integers of size n - 1, source and dest. The i-th road connects town source[i] to town dest[i]. The roads are bidirectional.

You’re also given a list of integers population of size n, where population[i] represents the population of the i-th town.

You are looking to upgrade some number of towns into cities.

However, there is a catch: no two cities should be adjacent to each other due to fierce competition, and every node adjacent to a town should be a city to allow easier access to infrastructure. In other words, every road must connect a town and a city.

What is the maximum possible population of all the cities?

Constraints

n ≤ 10,000
Example 1
Input
source = [0, 0, 2, 2]
dest = [1, 2, 4, 3]
population = [5, 7, 3, 2, 4]
Output
11
Explanation
We can upgrade cities 0, 3, and 4 to get a population of 11.
"""

class Solution:
    def solve(self, source, dest, population):
        graph = collections.defaultdict(list)
        for i in range(len(source)):
            graph[source[i]].append(dest[i])
            graph[dest[i]].append(source[i])
        
        q = [0]
        col = [-1] * len(population)
        col[0] = 1
        while q:
            curr = q.pop(0)
            for v in graph[curr]:
                if col[v] == -1:
                    col[v] =1-col[curr]
                    q.append(v)
        a = 0
        b = 0
        for i in range(len(population)):
            if col[i] == 1:
                a += population[i]
            else:
                b += population[i]
        return max(a,b)

"""
TC = o(n)
"""