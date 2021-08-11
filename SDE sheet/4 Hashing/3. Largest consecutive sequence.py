"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Follow up: Could you implement the O(n) solution? 

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
In this we are first storing all the numbers in a hashmap,
then seeing if its increment value is present in the map or not.
"""
def longestConsecutive(self, nums: List[int]) -> int:
    if nums == []:
        return 0
    ans = 0
    dic = {}
    for i in nums:
        dic[i] = 1
    for i in nums:
        if i - 1 in dic:
            continue
        else:
            cnt = 1
            temp= i
            while temp + 1 in dic:
                cnt += 1
                temp += 1
            ans = max(ans,cnt)
    return ans
"""
TC = o(n)
SC = o(n)
"""