"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?

nums = [3,1,3,4,2]
Output: 3
"""
#Hare and Tortoise method
def findDuplicate(self, nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]
    slow = nums[slow]
    fast = nums[nums[fast]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    fast = nums[0]
    while slow!=fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
#swap sort method for both first missing positive and duplicate number
def swapsort(nums):
    n = len(nums)
    for i in range(n):
        correctPos = nums[i] - 1
        while 1 <= nums[i]  <= n and nums[i] != nums[correctPos]:
            nums[i],nums[correctPos] = nums[correctPos],nums[i]
            correctPos = nums[i]-1
    #print(nums)
    for i in range(n):
        if i + 1 != nums[i]:
            return nums[i]
"""
TC = O(n)
SC = O(1)
"""