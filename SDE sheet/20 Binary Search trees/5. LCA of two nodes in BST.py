"""
Given a Binary Search Tree (with all values unique) and two node values. Find the Lowest Common Ancestors of the two nodes in the BST.

Example 1:

Input:
              5
           /    \
         4       6
        /         \
       3           7
                    \
                     8
n1 = 7, n2 = 8
Output: 7

For Binary search tree, while traversing the tree from top to bottom the first node which lies in between the two numbers n1 and n2 is the LCA of the nodes,
i.e. the first node n with the lowest depth which lies in between n1 and n2 (n1<=n<=n2) n1 < n2. So just recursively traverse the BST in,
if node's value is greater than both n1 and n2 then our LCA lies in the left side of the node, if it's is smaller than both n1 and n2, then LCA lies on the right side. Otherwise,
the root is LCA (assuming that both n1 and n2 are present in BST)
"""
def LCA(root, n1, n2):
    #code here.
    if not root:
        return root
    if root.data > n1 and root.data > n2:
        return LCA(root.left,n1,n2)
    if root.data < n1 and root.data < n2:
        return LCA(root.right,n1,n2)
    return root
"""
TC = o(n)
SC = o(1)
"""