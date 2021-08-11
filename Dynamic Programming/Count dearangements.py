"""
DP based problem 
A Derangement is a permutation of n elements, such that no element appears in its original position. For example, a derangement of {0, 1, 2, 3} is {2, 3, 1, 0}.
"""
def solve(n):
    dp = [0 for i in range(n+1)]
    dp[1] = 0
    dp[2] = 1
    for i in range(3,n+1):
        dp[i] =  (i-1) * (dp[i-1] + dp[i-2])
    return dp[n]
print(solve(4))
