"""
we use extra space in this
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        
        elif x <= self.min[-1]:
            self.min.append(x)
        
    def pop(self) -> None:
        if not self.stack:
            return -1
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
            
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min:
            return -1
        else:
            return self.min[-1]
"""
TC for all operations = o(1)
SC = o(n)
"""
"""
Without extra space
"""
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
