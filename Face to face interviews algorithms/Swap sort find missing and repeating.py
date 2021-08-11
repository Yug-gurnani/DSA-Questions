#complexity = 2n-2 = o(n)
arr = [2,3,1,5,1]
i = 0
n = len(arr)
miss = []
repeat = []
while i < n:
    if arr[i] != arr[arr[i]-1]:
        arr[i],arr[arr[i]-1] = arr[arr[i]-1],arr[i]
    else:
        i += 1
for i in range(len(arr)):
    if arr[i]!= i+1:
        miss.append(i+1)
        repeat.append(arr[i])
print(miss,repeat)
    