arr = [1,2,3]
s = 0
n = len(arr)
for i in range(len(arr)):
    s += arr[i] * (i+1) * (n-i)
print(s)
