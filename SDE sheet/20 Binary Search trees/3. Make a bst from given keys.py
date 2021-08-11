"""
Given a sorted array. Convert it into a Height balanced Binary Search Tree (BST).
Height balanced BST means a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Input: nums = {1, 2, 3, 4}
Output: {2, 1, 3, 4}
Explanation: 
The preorder traversal of the following 
BST formed is {2, 1, 3, 4}:
     3
    /  \
   2    4
 /
1
"""
class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
class Solution:
	def sortedArrayToBST(self, nums):
		#Code here
		def create(nums,low,high,root):
		    if not nums or low > high:
		        return root
		    
		    mid = low + (high-low)//2
		    root = Node(nums[mid])
		    root.left = create(nums,low,mid-1,root.left)
		    root.right = create(nums,mid + 1,high,root.right)
		    return root
		root = create(nums,0,len(nums)-1,None)
	    ans = []
        def pre(root,ans):
            if not root:
                return
            ans.append(root.data)
            if root.left:
                pre(root.left,ans)
            if root.right:
                pre(root.right,ans)
        pre(root,ans)
        return ans
"""
TC = o(n) or o(n log n) in case of unsorted array
SC = o(n) for result
"""