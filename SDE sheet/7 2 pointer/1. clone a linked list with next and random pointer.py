"""
Revise carefully


A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

To avoid using of extra space we have used two pointer.
"""
def copyRandomList(self, head: 'Node') -> 'Node':
    # First round: make copy of each node,
        # and link them together side-by-side in a single list.
    it = head
    front = head
    while it:
        front = it.next
        copy = Node(it.val)
        it.next = copy
        copy.next = front
        it = front
    #Second round: assign random pointers for the copy nodes.
    it = head
    while it:
        if it.random != None:
            it.next.random = it.random.next
        it = it.next.next
    #// Third round: restore the original list, and extract the copy list.    
    ans = Node(0)
    temp = ans
    it = head
    while it:
        front = it.next.next
        temp.next = it.next
        it.next = front
        temp = temp.next
        it = it.next
    return ans.next
    
"""
TC = o(n)
SC = o(1)
"""