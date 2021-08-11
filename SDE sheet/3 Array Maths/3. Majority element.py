"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Follow-up: Could you solve the problem in linear time and in O(1) space?

In this we use MOORE's voting algorithm
as if a majority element exist 
it will be cancelling all other elements and will be left in the ele variable.
"""
def majorityElement(nums):
    cnt = 0
    ele = 0
    n = len(nums)
    for i in range(n):
        if cnt == 0:
            ele = nums[i]
        if ele == nums[i]:
            cnt  += 1
        else:
            cnt -= 1
    return ele
print(majorityElement([1,2,3]))