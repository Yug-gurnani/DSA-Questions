"""
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

Example 1:

Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element 
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
since it doesn't exist, it is -1.
"""
def nextLargerElement(arr,n):
    stack = []
    arr = arr[::-1]
    ans = []
    for i in arr:
        while stack and stack[-1] < i:
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