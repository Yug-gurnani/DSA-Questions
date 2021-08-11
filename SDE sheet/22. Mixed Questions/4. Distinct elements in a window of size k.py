"""
Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.

Example 1:

Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: Window 1 of size k = 4 is
1 2 1 3. Number of distinct elements in
this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number
of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number
of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number
of distinct elements in this window are 3.
"""
def countDistinct(arr, n, k):
    # Code here
    l = 0
    r = 0
    dic = {}
    ans = []
    count = 0
    while r < n:
        #print(dic,count)
        if arr[r] not in dic:
            dic[arr[r]] = 1
            count += 1
        else:
            dic[arr[r]] += 1
        if r - l + 1 < k:
            r += 1
        elif r - l + 1 == k:
            ans.append(count)
            dic[arr[l]] -= 1
            if dic[arr[l]] == 0:
                del dic[arr[l]]
                count -= 1
            l += 1
            r += 1
    return ans
"""
TC = o(n)
SC = o(n)
"""