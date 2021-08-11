"""
Given a BST and a key K. If K is not present in the BST, Insert a new Node with a value equal to K into the BST. 

Example 1:

Input:
     2
   /   \
  1     3
K = 4
Output: 1 2 3 4
Explanation: After inserting the node 4
Inorder traversal will be 1 2 3 4.
"""
def insert(root, key):
    # code here
    ans = [None]
    if not root:
        return
    def solve(root,key,ans):
        if not root:
            ans = [None]
            return
        if root.data > key:
            solve(root.left,key,ans)
        if root.data < key:
            solve(root.right,key,ans)
        if root.data == key:
            ans = [True]
            return
    solve(root,key,ans)
    if ans[0] == True:
        return root
    else:
        def ins(root,key):
            if not root:
                return
            if root.data < key:
                if not root.right:
                    root.right = Node(key)
                    return
                else:
                    ins(root.right,key)
            if root.data > key:
                if not root.left:
                    root.left = Node(key)
                else:
                    ins(root.left,key)
        ins(root,key)
        return root
"""
TC = o(n)
SC = o(1)
"""