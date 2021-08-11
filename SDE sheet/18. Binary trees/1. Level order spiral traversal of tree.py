"""
Complete the function to find spiral order traversal of a tree.

Input:
           10
         /     \
        20     30
      /    \
    40     60
Output: 10 20 30 60 40 
like for odd number levels reverse the order of the elements and for even number remain it as it is
"""
from collections import deque
# your task is to complete this function
# function should print the level order traversal of the binary tree in spiral order
# Note: You aren't required to print a new line after every test case
def findSpiral(root):
    # Code here
    if not root:
        return []
    q = deque([root])
    ans = []
    arr = [root.data]
    level = 1
    while q:
        curr = q[0]
        if len(q) == len(arr):
            if level % 2:
                arr = arr[::-1]
            ans.extend(arr)
            level += 1
            arr = []
        if curr.left:
            q.append(curr.left)
            arr.append(curr.left.data)
        if curr.right:
            q.append(curr.right)
            arr.append(curr.right.data)
        q.popleft()
    return ans
"""
TC = o(n)
SC = o(n)
"""