arr = [1,3,2,0,0,4,8]
stack = []
ans = []
arr = arr[::-1]
for i in arr:
    if stack == []:
        ans.append(-1)
    elif stack[-1] > i:
        ans.append(stack[-1])
    else:
        while stack and stack[-1] <= i:
            stack.pop()
        if stack == []:
            ans.append(-1)
        elif stack[-1] > i:
            ans.append(stack[-1])
    stack.append(i)
print(ans[::-1])