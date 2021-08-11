arr = []
sup = []
def push(arr,n):
    arr.append(n)
    if not sup:
        sup.append(n)
    elif sup[-1] >= n:
        sup.append(n)
def pop(arr):
    temp = arr.pop()
    if temp == sup[-1]:
        sup.pop()
def getmin(arr):
    if not sup:
        return -1
    return sup[-1]    
