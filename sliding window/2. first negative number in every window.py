from collections import deque
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    k = int(input())
    i = 0
    j = 0
    ans = deque([])
    final = []
    i = 0
    j = 0

    while i <= n-k and j  < n:
        if arr[j] < 0:
            ans.append(arr[j])
        if j -i+1 < k:
            j += 1
        else:
            if ans:
                final.append(ans[0])
            else:
                final.append(0)
            if ans:
                if ans[0] == arr[i]:
                    ans.popleft()
            i += 1
            j += 1
        
    print(*final)