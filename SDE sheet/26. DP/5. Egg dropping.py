"""
Suppose you have N eggs and you want to determine from which floor in a K-floor
building you can drop an egg such that it doesn't break. You have to determine the minimum number of attempts
you need in order find the critical floor in the worst case while using the best strategy.There are few rules given below. 

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the eggs breaks at a certain floor, it will break at any floor above.
For more description on this problem see wiki page

Example 1:

Input:
N = 2, K = 10
Output: 4
"""
def solve(e,f,dp):
    if e == 1 or f == 0 or f == 1:
        dp[f][e] = f
        return dp[f][e]
    if dp[f][e] != -1:
        return dp[f][e]
    mn = float('inf')
    for k in range(1,f):
        temp = 1+max(solve(e-1,k-1,dp),solve(e,f-k,dp))
        '''
        1st condition is when we have to check all bottom floors and we have now e-1 eggs left and k-1 floors left
        2nd condition the egg doesnt break and we have to all eggs remaining and we have to check all upper floors i.e. f-k floors
        '''
        mn = min(mn,temp)
    dp[f][e] = mn
    return dp[f][e]
dp = [[-1 for i in range(3)]for i in range(5)] 
print(solve(2,4,dp))