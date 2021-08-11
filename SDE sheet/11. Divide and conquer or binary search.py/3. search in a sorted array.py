"""
The first line of the input contains an integer T, denoting the total number of test cases.
Then T test cases follow. Each test case consists of three lines.
First line of each test case contains an integer N denoting the size of the given array.
Second line of each test case contains N space separated integers denoting the elements of the array A.
Third line of each test case contains an integer K denoting the element to be searched in the array.

Output:
Corresponding to each test case, output the index of the element found in the array.  If element is not present, then output -1.
"""
def binarysearch(arr,low,high,ele):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            high = mid - 1
        else:
            low = mid + 1
    return -1
def find_min_element(arr,n):
    low = 0
    high = n-1
    if n == 1:
        return 0
    while low <= high:
        if arr[low] <= arr[high]:
            return low
        mid = low + (high - low) // 2
        prev = (mid + n - 1 )% n
        nex = (mid + 1) % n
        if arr[mid] < arr[prev] and arr[mid] < arr[nex]:
            return mid
        elif arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1
arr = [4,5,6,7,1,2,3]
n = 7
ele = 8
m = find_min_element(arr,n)
a = binarysearch(arr,0,m-1,ele)
b = binarysearch(arr,m,n-1,ele)
if a == -1 and b == -1:
    print("not found")
else:
    print(max(a,b))
"""
TC = o(log n)
SC = o(1)
"""
