arr = [1,3,2,0,0,4,8]
stack = []
res = []
for i in arr:
    while stack and stack[-1] >= i:
        stack.pop()
    if not stack:
        res.append(-1)
    else:
        res.append(stack[-1])
    stack.append(i)
print(res)