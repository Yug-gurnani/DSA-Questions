"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

based on 2 sum and 4 sum
"""
def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = n-1
        while j < k:
            temp = nums[i] + nums[j] + nums[k]
            if temp > 0:
                k -= 1
            elif temp < 0:
                j += 1
            else:
                ans.append([nums[i],nums[j],nums[k]])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1
                k -= 1
    return ans
"""
TC = o(n^2)
SC = o(1)
"""