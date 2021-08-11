"""
Given two sorted arrays arr1[] and arr2[] of sizes N and M in non-decreasing order.
Merge them in sorted order without using any extra space.
Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements. 

Input: 
N = 4, arr1[] = [1 3 5 7] 
M = 5, arr2[] = [0 2 6 8 9]
Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]
Explanation: After merging the two 
non-decreasing arrays, we get, 
0 1 2 3 5 6 7 8 9.
"""
"""
In this we use GAP method or shell sort method to sort thia array in o(1) space
"""
import math
def merge(arr1,arr2,n,m):
    #code here
    gap = math.ceil((n+m)/2)
    #print(arr1,arr2)
    while gap:
        i = 0
        j = gap
        while j < (n+m):
            #print(arr1,arr2)
            if j >= n:
                temp = j - n
                if i >= n:
                    temp1 = i - n
                    if arr2[temp1] > arr2[temp]:
                        arr2[temp1],arr2[temp] = arr2[temp],arr2[temp1]
                else:
                    if arr1[i] > arr2[temp]:
                        arr1[i],arr2[temp] = arr2[temp],arr1[i]
            else:
                if arr1[i] > arr1[j]:
                    arr1[i],arr1[j] = arr1[j],arr1[i]
            i += 1
            j += 1
        if gap == 1:
            break
        gap = math.ceil(gap/2)
        #print(arr1,arr2)
"""
TC = O((n+m)*log(n+m)) log because of the gap
SC = O(1)
"""