"""
Given an array of size n such that each element contains either a 'P' for policeman or a 'T' for thief.
Find the maximum number of thieves that can be caught by the police. 
Keep in mind the following conditions :

Each policeman can catch only one thief.
A policeman cannot catch a thief who is more than K units away from him.
Example 1:

Input:
N = 5, K = 1
arr[] = {P, T, T, P, T}
Output: 2
Explanation: Maximum 2 thieves can be 
caught. First policeman catches first thief 
and second police man can catch either second 
or third thief.
"""
def catchThieves(self, arr, n, k): 
    pol = []
    thi = []
    for i in range(n):
        if arr[i] == "P":
            pol.append(i)
        else:
            thi.append(i)
    l = 0
    r = 0
    ans = 0
    while l < len(thi) and r < len(pol):
        if abs(thi[l] - pol[r]) <= k:
            ans += 1
            l += 1
            r += 1
        elif thi[l] < pol[r]:
            l += 1
        else:
            r += 1
    return ans