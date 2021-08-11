"""
You are given an array of integers nums,
there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 We used a deque because it can perform both popleft and pop in o(1) time and we need to store the next maximum in it.
 IT is basically a preprocessing of the answers. that after one the other answer is ready
"""
from collections import deque
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = deque([])
    ans = []
    window = []
    l = 0
    r = 0
    n = len(nums)
    while r < n:
        #print(q)
        while q and q[-1] < nums[r]:
            q.pop()
        q.append(nums[r])
        if r-l+1 < k:
            r += 1
            continue
        elif r - l + 1 == k:
            ans.append(q[0])
            if nums[l] == q[0]:
                q.popleft()
        l += 1
        r += 1
    return ans
"""
TC = o(n)
SC = o(n)
"""