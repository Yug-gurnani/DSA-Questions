'''
Given a binary tree root, 
return the length of the longest path consisting of consecutive values between any two nodes in the tree.
The path can be consecutively increasing or decreasing.
Input
Visualize
root =
2

1

3

4

0

5

Output
5
Explanation
A longest path is [1, 2, 3, 4, 5].
'''
def solve(self, root):
        ans = []
        res = 0
        def s(root):
            nonlocal res
            if not root:
                return 0,0
            linc,ldec = s(root.left)
            rinc,rdec = s(root.right)

            if not root.left or root.left.val + 1 != root.val:
                linc = 0
            if not root.left or root.left.val - 1 != root.val:
                ldec = 0
            if not root.right or root.right.val + 1 != root.val:
                rinc = 0
            if not root.right or root.right.val - 1 != root.val:
                rdec = 0
            res = max(res, 1+ldec+rinc,1 + rdec + linc)
            return max(1 + linc,1+rinc),max(1 + ldec, 1+ rdec)
        s(root)
        return res
