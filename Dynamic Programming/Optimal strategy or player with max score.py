"""
Given an array arr of non-negative integers of size N, 2 players are playing a game.
In each move, a player chooses an element from either end of the array, and the size of the array shrinks by one.
Both players take alternate chances and the game continues until the size of the array becomes 0. Every time a
player chooses an array element the array value is added to the player's score. At the need player with maximum score wins.
You have to predict whether player 1 will win the game or not. Both players will play optimally.

N = 3
arr[] = {2,6,3}
Output:
0 
Explanation:
Initially, player 1 can choose between 2 and 3. 
If he chooses 3 (or 2), then player 2 can choose 
from 2 (or 3) and 6. If player 2 chooses 6,
then player 1 will be left with 2 (or 3). 
So, final score of player 1 is 2 + 3 = 5,
and player 2 is 6. 
Hence, player 1 will never be the winner and 
output is 0.
"""
class Solution:
    def is1winner (self, n, arr):
        # code here
        dp = [[0 for i in range(n+1)]for i in range(n+1)]
        for g in range(n):
            for j in range(g,n):
                i = j - g
                x = 0
                if((i + 2) <= j): 
                    x = dp[i + 2][j] 
                y = 0
                if((i + 1) <= (j - 1)): 
                    y = dp[i + 1][j - 1] 
                z = 0
                if(i <= (j - 2)): 
                    z = dp[i][j - 2]
                val1 = arr[i] + min(x,y)
                val2 = arr[j] + min(y,z)
                dp[i][j] = max(val1,val2)
        s = sum(arr)
        rem = s-dp[0][n-1]
        if dp[0][n-1] < rem:
            return False
        return True
"""
TC = o(N*N)
SC = o(N*N)
"""
