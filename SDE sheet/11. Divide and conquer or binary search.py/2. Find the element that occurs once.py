"""
Given a sorted array arr[] of size N. Find the element that appears only once in the array. All other elements appear exactly twice. 

Example 1:

Input:
N = 11
arr[] = {1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65}
Output: 4
Explanation: 4 is the only element that 
appears exactly once.


An Efficient Solution can find the required element in O(Log n) time. The idea is to use Binary Search.
Below is an observation in the input array. 
All elements before the required have the first occurrence at even index (0, 2, ..) and next occurrence at odd index (1, 3, …).
And all elements after the required elements have the first occurrence at odd index and next occurrence at even index. 
1) Find the middle index, say ‘mid’.
2) If ‘mid’ is even, then compare arr[mid] and arr[mid + 1]. If both are the same, then the required element after ‘mid’ else before mid.
3) If ‘mid’ is odd, then compare arr[mid] and arr[mid – 1]. If both are the same, then the required element after ‘mid’ else before mid.
"""
def findOnce(self,arr : list, n : int):
        # Complete this function
    def search(arr,low,high):
        print(low,high)
        if low > high:
            return None
        if low == high:
            return arr[low]
            return 
        mid = low + (high-low)//2
        if mid % 2==0:
            if arr[mid] == arr[mid+1]:
                
                search(arr,mid+2,high)
            else:
                search(arr,low,mid)
        else:
            if arr[mid] == arr[mid-1]:
                
                search(arr,mid+1,high)
            else:
                search(arr,low,mid-1)
        ans = search(arr,0,n-1)
        return ans
"""
TC = o(log base 2 (n))
SC = o(1)
"""