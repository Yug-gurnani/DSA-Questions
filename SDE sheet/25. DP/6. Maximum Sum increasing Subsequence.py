"""
Given an array arr of N positive integers, the task is to find the maximum sum increasing subsequence of the given array.

Example 1:

Input: N = 5, arr[] = {1, 101, 2, 3, 100} 
Output: 106
Explanation:The maximum sum of a
increasing sequence is obtained from
{1, 2, 3, 100}

It is a slight variation of the LIS problem all we have to do that we will use the arr values instead of length 

"""
def maxSumIS(self, arr, n):
    # code here
    dp = arr.copy()
    
    for i in range(1,n):
        for j in range(i):
            if arr[i] > arr[j]:
                if dp[i] < dp[j] + arr[i]:
                    dp[i] = dp[j] + arr[i]
    #print(dp)
    return max(dp)
"""
TC = o(n^2)
SC = o(n)
"""