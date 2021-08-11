"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Approach is this first we level order traverse the tree and store it in the string and for case like negative or large number we store them in a # to #
binding and connect them again as it is stored in level order in deserialize
"""
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"
        s = ""
        q = deque([root])
        if root.val < 0 or root.val > 9:
            s += "#"
            s += str(root.val)
            s += "#"
        else:
            s += str(root.val)
        while q:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
                if curr.left.val < 0 or curr.left.val > 9:
                    s += "#"
                    s += str(curr.left.val)
                    s += "#"
                else:
                    s += str(curr.left.val)
            else:
                s += "N"
            if curr.right:
                q.append(curr.right)
                if curr.right.val < 0 or curr.right.val > 9:
                    s += "#"
                    s += str(curr.right.val)
                    s += "#"
                else:
                    s += str(curr.right.val)
            else:
                s += "N"
        print(s)
        return s
        

    def deserialize(self, s):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if s == "N":
            return None
        n = len(s)
        i = 0
        j = 1
        q = deque([])
        n = len(s)
        while i < n:
            if s[i] != "N" and s[i] != "#":
                q.append(TreeNode(int(s[i])))
            elif s[i] == "#":
                i += 1
                tmp = ""
                while s[i] != "#":
                    tmp += s[i]
                    i += 1
                q.append(TreeNode(tmp))
            else:
                q.append(None)
            i += 1
        
        root = q[0]
        print(root.val)
        j = 1
        i = 0
        n = len(q)
        while q and j < len(q):
            curr = q[i]
            if curr == None:
                i += 1
                continue
            if j < n:
                curr.left = q[j]
            j += 1
            if j < n:
                curr.right = q[j]
            j += 1
            i += 1
        return root
"""
TC = o(n)
SC = o(1)
"""