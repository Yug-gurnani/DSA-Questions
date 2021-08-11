"""
Professor X wants his students to help each other in the chemistry lab.
He suggests that every student should help out a classmate who scored less marks than
him in chemistry and whose roll number appears after him. But the students are lazy and they don't want to search too far.
They each pick the first roll number after them that fits the criteria. Find the marks of the classmate that each student picks.
Note: one student may be selected by multiple classmates.

Example 1:

Input: N = 5, arr[] = {3, 8, 5, 2, 25}
Output: 2 5 2 -1 -1

"""
from collections import deque
class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        stack = deque()
        ans = []
        for i in range(n-1,-1,-1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(arr[i])
        return ans[::-1]
"""
TC = o(n)
SC = o(n)
"""