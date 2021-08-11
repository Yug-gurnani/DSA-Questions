"""
Given an unsorted array arr[] of size N, rotate it by D elements in the counter-clockwise direction. 

 

Example 1:

Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.

reverse(a, a+d) Reverse array from beginning till D
reverse(a+d, a+n) Reverse array from D till N
reverse(a, a+n) Reverse the whole array
"""
def rotateArr(a,d,n):
    def reverse(i,j,arr):
        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
    reverse(0,d-1,a)
    reverse(d,n-1,a)
    reverse(0,n-1,a)