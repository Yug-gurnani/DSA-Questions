"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B becomes a substring of the repeated A.
If B cannot be a substring of A no matter how many times it is repeated, return -1.

Example 1:

Input: A = "abcd", B = "cdabcdab"
Output: 3
Explanation: After repeating A three times, 
we get "abcdabcdabcd".
"""
def repeatedStringMatch(self, a, b):
    n,m = len(a),len(b)
    for i in range(n):
        if a[i] == b[0]:
            k = i
            count = 1
            for j in range(m):
                if k >= len(a):
                    k = 0
                    count += 1
                
                if a[k]!=b[j]:
                    break
                k += 1
            else:
                return count
    return -1