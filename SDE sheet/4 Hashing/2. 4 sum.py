"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

"""

def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    ans = []
    nums.sort()
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-2):
            if j > 0 and nums[j] == nums[j-1] and j-1 != i:
                continue
            l = j +1
            r = len(nums)-1
            while l < r:
                temp = nums[i]+nums[j]+nums[l]+nums[r]
                if temp < target:
                    l += 1
                elif temp > target:
                    r -= 1
                else:
                    ans.append([nums[i],nums[j],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r-= 1
    return ans
"""
TC = o(n^3 + n log n)
sc = o(1)
"""