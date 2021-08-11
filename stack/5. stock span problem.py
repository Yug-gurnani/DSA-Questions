arr = [100,80,60,70,60,75,85]
stack = []
ans = []
for i in range(len(arr)):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if not stack:
        ans.append(i+1)
    else:
        ans.append(i+1-len(stack))
    stack.append(arr[i])
#print(stack)
print(ans)