"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.
"""
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    i = j = 0
    n = len(nums)
    m = 0
    while i < n and j < n:
        if nums[i] == 1:
            j = i
            while j < n and nums[j] == 1:
                j += 1
            m = max(j-i,m)
            i = j
        else:
            i += 1
    m = max(j-i,m)
    return m
"""
TC = o(n)
SC = o(1)
"""