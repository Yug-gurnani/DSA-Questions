"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
def sortColors( nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    a = 0
    b = 0
    c = 0
    for i in nums:
        if i == 0:
            a+=1
        if i == 1:
            b+=1
        if i == 2:
            c += 1
    i = 0
    while a:
        nums[i] = 0
        a -= 1
        i += 1
    while b:
        nums[i] = 1
        b -= 1
        i += 1
    while c:
        nums[i] = 2
        c -= 1
        i += 1
"""
TC = O(n)
SC = O(1)
"""