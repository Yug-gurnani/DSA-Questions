'''
two conditions:
1st by using simple kadane algo 
2nd by using wrap around property
i.e. sum(arr) - min_subarray_sum
by inverting all elements

''' 
def kadane(a):
    lsum = 0
    gsum = 0
    for i in range(len(a)):
        lsum += a[i]
        if lsum < 0:
            lsum = 0
        if lsum > gsum:
            gsum = lsum
    return gsum
def max_wrap(arr,n):
    max_kadane = kadane(arr)
    max_wra = 0
    for i in range(n):
        max_wra += arr[i]
        arr[i] = -arr[i]
    max_wra += kadane(arr)
    return max(max_kadane,max_wra)
    
for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 1:
        print(arr[0])
    elif all(i < 0  for i in arr):
        print(max(arr))
    else:
        print(max_wrap(arr,n)) 