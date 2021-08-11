"""
Just do a preorder traversal and swap the nodes
"""
def invertTree(self, root: TreeNode) -> TreeNode:
    def solve(root):
        if not root:
            return
        if root.left and root.right:
            root.left,root.right = root.right,root.left
        elif root.left and not root.right:
            root.right = root.left
            root.left = None
        elif root.right and not root.left:
            root.left = root.right
            root.right = None
        solve(root.left)
        
        solve(root.right)
    solve(root)
    return root