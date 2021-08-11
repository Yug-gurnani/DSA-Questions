def maut_ka_khel(index,n,k,arr):
    if n == 1:
        return 
    index = (index + k) % n
    del arr[index]
    maut_ka_khel(index,n-1,k,arr)
    
    
for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = [x for x in range(1,n+1)]
    maut_ka_khel(0,n,k-1,arr)
    print(arr[0])