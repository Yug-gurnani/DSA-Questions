"""
Given an array arr[] of n integers. Count the total number of sub-array having total distinct elements same as that of total distinct elements of the original array.
"""
def countDistinctSubarray(arr, n): 
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1
    k = len(dic)
    dic = {}
    ans = 0
    right = 0
    window = 0
    for left in range(n):
        while right < n and window < k:
            if arr[right] in dic:
                dic[arr[right]] += 1
            else:
                dic[arr[right]] = 1
            if dic[arr[right]] == 1:
                window += 1
            right += 1
        if window == k:
            ans += n - right + 1
        dic[arr[left]] -= 1
        if dic[arr[left]] == 0:
            window -= 1
    return ans