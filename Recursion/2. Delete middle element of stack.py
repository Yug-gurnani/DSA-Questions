stack = [1,2,3,4,5,6]
n = len(stack)
k = (n//2) + 1
def solve(stack,n,k):
    if n == 0:
        return
    if n == k:
        stack.pop()
        return
    temp = stack.pop()
    solve(stack,n-1,k)
    stack.append(temp)
solve(stack,n,k)
print(stack)