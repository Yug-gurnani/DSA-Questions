"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
def solve(arr,n):
    lsum = arr[0]
    gsum = arr[0]
    for i in range(1,n):
        lsum = max(arr[i],lsum + arr[i])
        gsum = max(lsum,gsum)
    return gsum
 """
TC = O(n)
SC = O(1)
"""