import math
for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()

    def solve(n,k,s):
        ans = 0
        i = 0
        j = n-1
        tmp = chr(96+k)
        mid = math.ceil(n/2)
        while i <= j:
            
            diff = ord(min(s[i],s[j],tmp)) - 97
            #print(diff * (k ** (mid - (i + 1))))
            ans += diff * (k ** (mid - (i + 1)))
            i += 1
            j -= 1
        return ans 
    ans = solve(n,k,s)
    if n == 1:
        print("Case #{}: {}".format(_+1,min(k,ord(s)-97)))
    else:
        print("Case #{}: {}".format(_+1,ans+1))
