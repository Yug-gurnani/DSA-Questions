"""
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
"""
#Your should return the required output
def maxLen(n, arr):
    #Code here
    dic = {}
    ans = 0 
    s = 0
    for i in range(n):
        s += arr[i]
        if s == 0:
            ans = max(ans,i-0+1)
        elif s in dic:
            ans = max(i - dic[s],ans)
        else:
            dic[s] = i
    #if s == 0:    ans = max(ans,)
    return ans
"""
TC = o(n)
sc = o(n)
"""
