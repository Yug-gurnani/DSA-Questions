def insert(arr,temp):
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return 
    val = arr.pop()
    insert(arr,temp)
    arr.append(val)
arr = [2,4,0,1,5,6]
def sorting(arr):
    if len(arr) == 0:
        return
    temp = arr.pop()
    sorting(arr)
    insert(arr,temp)
sorting(arr)
print(arr)



