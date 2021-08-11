"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "snakesandladder",
dict = ["snake", "snakes", "and", "sand", "ladder"].

A solution is ["snakes and ladder",
           "snake sand ladder"].
"""
def solve(dic,n,s,res,ans):
    ss = len(s)
    for i in range(1,ss+1):
        sub = s[:i]
        if sub not in dic:
            continue
        else:
            if i == ss:
                res += sub
                ans.append(res)
                return
            solve(dic,n,s[i:],res+sub+" ",ans)
for _ in range(int(input())):
    n = int(input())
    dic = {}
    arr = list(map(str,input().split()))
    for i in arr:
        dic[i] = 1
    ans = []
    s = input()
    solve(dic,n,s,"",ans)
    if ans == []:
        print("EMPTY")
    else:
        ans.sort()
        for i in range(len(ans)):
            print("(",end = "")
            for j in range(len(ans[i])):
                print(ans[i][j],end = "")
            print(")",end = "")
        print()
"""
TC = o(n*s)
SC = o(1)
"""