"""
Think brute force before optimal solution
"""
def minswaps(self,s):
    s = list(s)
    ss = s[::-1]
    n = len(s)
    def solve(s,n):
    
        count = 0
        for i in range(n//2):
            left = i
            right = n - left - 1
            while left < right:
                if s[left] == s[right]:
                    break
                else:
                    right -= 1
            if left == right:
                return -1
            for j in range(right,n-left-1):
                count += 1
                s[j],s[j+1] = s[j+1],s[j]
        return count
    return max(solve(s,n),solve(ss,n))