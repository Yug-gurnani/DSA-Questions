#nearest smaller in right - nearest smaller in left -1  formula
arr = [6,2,5,4,5,1,6]
n = len(arr)
stack = []
left = []
right = []
ans = []
for i in range(n):
    while stack and stack[-1][0] >= arr[i]:
        stack.pop()
    if not stack:
        left.append(-1)
    else:
        left.append(stack[-1][1])
    stack.append([arr[i],i])
stack = []
for i in range(n-1,-1,-1):
    while stack and stack[-1][0] >= arr[i]:
        stack.pop()
    if not stack:
        right.append(n)
    else:
        right.append(stack[-1][1])
    stack.append([arr[i],i])
right = right[::-1]
for i in range(n):
    ans.append(right[i]-left[i]-1)
currmax = 0
for i in range(n):
    currmax = max(currmax,arr[i]*ans[i])
print(currmax)