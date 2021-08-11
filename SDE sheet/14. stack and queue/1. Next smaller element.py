"""
Given an array, print the Next Smaller Element (NSE) for every element.
The Smaller smaller Element for an element x is the first smaller element on the right side of x in array.
Elements for which no smaller element exist (on right side), consider next smaller element as -1.

Examples:
a) For any array, rightmost element always has next smaller element as -1.
b) For an array which is sorted in increasing order, all elements have next smaller element as -1.
c) For the input array [4, 8, 5, 2, 25}, the next smaller elements for each element are as follows.

Element       NSE
   4      -->   2
   8      -->   5
   5      -->   2
   2      -->   -1
   25     -->   -1
"""
def solve(arr,n):
    stack = []
    arr = arr[::-1]
    ans = []
    for i in arr:
        while stack and stack[-1] > i:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(i)
    return ans[::-1]
"""
TC = o(n)
SC = o(n)
"""