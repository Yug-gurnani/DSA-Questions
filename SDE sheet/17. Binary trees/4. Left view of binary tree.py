"""
Given a Binary Tree, print Left view of it.
Left view of a Binary Tree is set of nodes visible when tree is visited from Left side.
The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   

Example 1:

Input:
   1
 /  \
3    2
Output: 1 3
"""
def LeftView(root):
    if not root:
        return []
    q = [root]
    ans = []
    arr = [root.data]
    while q:
        curr = q[0]
        if len(q) == len(arr):
            ans.append(arr[0])
            arr = []
        if curr.left:
            q.append(curr.left)
            arr.append(curr.left.data)
        if curr.right:
            q.append(curr.right)
            arr.append(curr.right.data)
        q.pop(0)
    return ans
"""
TC = o(n)
SC = o(n)
"""