#to find max subarray sum
arr = [1,-1,3,-2,5]
lsum = arr[0]
gsum = arr[0]
for i in range(1,len(arr)):
    lsum = max(arr[0],lsum+arr[0])
    if lsum > gsum:
        gsum = lsum
print(gsum)