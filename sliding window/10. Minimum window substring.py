"""
Given two strings S and P. Find the smallest window in the S consisting of all the characters of P.

Example 1:

Input:
S = "timetopractice"
P = "toc"
Output: 
toprac
Explanation: "toprac" is the smallest
substring in which "toc" can be found.
"""
def smallestWindow(s, p):
    dic = {}
    count = 0
    for i in p:
        if i not in dic:
            dic[i] = 0
            count += 1
        dic[i] += 1
    i = 0
    j = 0
    ans = []
    n,m = len(s),len(p)
    if m > n:
        return -1
    while j < n:
        if count > 0:
            if s[j] in dic:
                dic[s[j]] -= 1
                if dic[s[j]] == 0:
                    count -= 1
            j += 1
        
        if count == 0:
            if not ans:
                ans = [i,j]
            else:
                if ans[1] - ans[0] > j - i:
                    ans = [i,j]
            while i < j and count <= 0:
                if s[i] in dic:
                    dic[s[i]] += 1
                    if dic[s[i]] == 1:
                        count += 1
                i += 1
            if ans[1] - ans[0] > j - i:
                ans = [i,j]
            
    #print(ans,i,j)
    if count == 0:
        if not ans:
            ans = [i,j]
        else:
            if ans[1] - ans[0] > j - i:
                ans = [i,j]
    if not ans:
        return -1
    return s[ans[0]-1:ans[1]]
"""
TC = o(n)
SC = o(m)
"""