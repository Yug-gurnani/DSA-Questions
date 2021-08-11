def countEvenSum(arr, n):
    # code here
    temp = [1,0]
    s = 0
    for i in range(n):
        s = ((s+arr[i])%2+2)%2
        temp[s] += 1
    res = 0
    res += (temp[0] * (temp[0]-1))//2
    res += (temp[1] * (temp[1]-1))//2
    return res