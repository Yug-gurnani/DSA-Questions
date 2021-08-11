"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

It is an optimized version of dp and we use binary search in this to reduce time complexity of linear search
"""
def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    time = list(zip(startTime,endTime,profit))
    time.sort(key = lambda x:x[1])
    def binary(time,i):
        low = 0
        high = i - 1
        while low <= high:
            mid = low + (high - low)//2
            if time[mid][1] <= time[i][0]:
                if time[mid+1][1] <= time[i][0]:
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1
        else:
            return -1
    n = len(profit)
    dp = [0 for i in range(n)]
    dp[0] = time[0][2]
    for i in range(1,n):
        inc = time[i][2]
        l = binary(time,i)
        if l != -1:
            inc += dp[l]
        dp[i] = max(inc,dp[i-1])
    #print(dp)
    return dp[n-1]
"""
TC = o(n lon n)
SC = o(n)
"""