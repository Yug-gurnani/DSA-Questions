"""
It is an extension of the previous problem 

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

Example 1:

Input: nums = [3,2,3]
Output: [3]
In this we also use MOORE's voting algorithm
we can see that maximum we can have 2 elements

so we take 2 elements num1 and num2
and apply extensive moore algorithm on that
so it will give us the two candidates
and at last we check that if they are the right candidates or not
"""
def majorityElement(nums: List[int]) -> List[int]:
    num1 = -1
    num2 = -1
    c1 = 0
    c2 = 0
    for i in range(len(nums)):
        if nums[i] == num1:
            c1 += 1
        elif nums[i] == num2:
            c2 += 1
        elif c1 == 0:
            num1 = nums[i]
            c1 = 1
        elif c2 == 0:
            
            num2 = nums[i]
            c2 = 1
        else:
            c1 -= 1
            c2 -= 1
    temp1 = 0
    temp2 = 0
    n = len(nums)
    for i in nums:
        if i == num1:
            temp1 += 1
        elif i == num2:
            temp2 += 1
    #print(temp1,temp2)
    if temp1 > n//3 and temp2 > n//3:
        return [num1,num2]
    elif temp1 > n//3:
        return [num1]
    elif temp2 > n//3:
        return [num2]
    else:
        return []
"""
TC = o(n)
SC = o(1)
"""

