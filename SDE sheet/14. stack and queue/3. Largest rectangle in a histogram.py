"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10

smaller on right - smaller on left - 1 formula

"""
def largestRectangleArea(arr: List[int]) -> int:
    left = []
    right = []
    n = len(arr)
    stack = []
    for i in range(n):
        while stack and stack[-1][0] >=arr[i]:
            stack.pop()
        if not stack:
            left.append(-1)
        else:
            left.append(stack[-1][1])
        stack.append([arr[i],i])
    stack = []
    for i in range(n-1,-1,-1):
        while stack and stack[-1][0]>=arr[i]:
            stack.pop()
        if not stack:
            right.append(n)#appending n because we have to take the area and if no smaller element then we add the n at the end so to cover the whole array
        else:
            right.append(stack[-1][1])
        stack.append([arr[i],i])
    ans = []
    right = right[::-1]
    for i in range(n):
        ans.append(right[i]-left[i]-1)
    m = 0
    for i in range(n):
        m = max(ans[i] * arr[i],m)
    return m
"""
TC = o(n)
SC = o(n)
"""