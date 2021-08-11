arr = [1,3,2,0,0,4,8]
stack = []
ans = []
for i in arr:
    if not stack:
        ans.append(-1)
    elif stack[-1] > i:
        ans.append(stack[-1])
    else:
        while stack and stack[-1] <= i:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
    stack.append(i)
print(ans)