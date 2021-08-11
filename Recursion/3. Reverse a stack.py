stack = [1,2,3,4,5]
n = len(stack)
def insert(stack,ele):
    print(stack)
    if stack == []:
        stack.append(ele)
        return 
    temp = stack.pop()
    insert(stack,ele)
    
    stack.append(temp)
def solve(stack,n):
    if n == 0:
        return
    temp = stack.pop()
    solve(stack,n-1)
    insert(stack,temp)
solve(stack,n)
print(stack)