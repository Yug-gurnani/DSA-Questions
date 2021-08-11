"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 0
    for j in range(1,n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i+1
"""
TC = o(n)
SC = o(1)
"""