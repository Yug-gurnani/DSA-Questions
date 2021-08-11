def findNumberOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1 for i in range(n)]
    count = dp.copy()
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
                    count[i] = count[j]
                elif dp[i] == dp[j] + 1:
                    count[i] += count[j]
    tmp = max(dp)
    res = 0
    for i in range(n):
        if dp[i] == tmp:
            res += count[i]
            
    return res