"""
Given an array that contains both positive and negative integers,
find the product of the maximum product subarray.
Expected Time complexity is O(n) and only O(1) extra space can be used.


It is similar to Largest Sum Contiguous Subarray problem. The only thing to note here is,
maximum product can also be obtained by minimum (negative) product ending with the previous element multiplied by this element.
For example, in array {12, 2, -3, -5, -6, -2}, when we are at element -2,
the maximum product is multiplication of, minimum product ending with -6 and -2. 
"""
def maxProduct(self, nums: List[int]) -> int:
    ma = nums[0]
    mi = nums[0]
    ans = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < 0:
            ma,mi = mi,ma # because by multiplying with the negative Value the bigger number get small and smaller number gets big.
        ma = max(nums[i],ma * nums[i])
        mi = min(nums[i],mi * nums[i])
        ans = max(ans,ma)
    return ans
"""
TC = o(n)
SC = o(1)
"""