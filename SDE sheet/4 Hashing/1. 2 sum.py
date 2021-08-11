"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
def twoSum(self, nums: List[int], k: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            return [i,dic[nums[i]]]
        else:
            dic[k - nums[i]] = i
"""
TC = o(n)
SC = o(n)
"""