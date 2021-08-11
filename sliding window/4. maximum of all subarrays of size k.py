from collections import deque
def max_of_subarrays(arr,n,k):
    ans = []
    temp = deque([])
    i = 0
    j = 0
    while j < n:
        
        while temp and temp[-1] < arr[j]:
            temp.pop()
        temp.append(arr[j])
        if j - i + 1 < k:
            j += 1
        else:
            ans.append(temp[0])
            if arr[i] == temp[0]:
                temp.popleft()
            i += 1
            j += 1
    return ans