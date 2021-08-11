def wordBreak(s, dictionary):
    # Complete this function
    dp = [-1 for i in range(len(s)+1)]
    def wordb(s,dictionary,dp):
        n = len(s)
        if n == 0:
            return 1
        if dp[n] == -1:
            dp[n] = 0
            for i in range(1,len(s)+1):
                sub = s[:i]
                if sub not in dictionary:
                    continue
                if wordb(s[i:],dictionary,dp):
                    dp[n] = 1
                    return 1
        return dp[n]
    return wordb(s,dictionary,dp)