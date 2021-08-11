currmin = None
def push(stack,ele):
    global currmin
    if not stack:
        stack.append(ele)
        currmin = ele
    else:
        if ele < currmin:
            stack.append(2 * ele - currmin)
            currmin = ele
        else:
            stack.append(ele)
def pop(stack):
    global currmin
    if not stack:
        print(-1)
        return 
    temp = stack.pop()
    if temp < currmin:
        currmin = 2*currmin - temp

def getmin(stack):
    print(stack)
    global currmin
    if not stack:
        print(-1)
        return
    print(currmin)
def top(stack):
    global currmin
    if stack[-1] < currmin:
        print(currmin)
    else:
        print(stack[-1])
stack = []
push(stack,5)
push(stack,3)
push(stack,7)
push(stack,1)
getmin(stack)
pop(stack)
getmin(stack)
pop(stack)
getmin(stack)
pop(stack)
getmin(stack)