"""
Given a Binary Search Tree (BST) and a positive integer k, find the k’th smallest element in the Binary Search Tree.
For example, in the following BST, if k = 3, then output should be 10, and if k = 5, then output should be 14.
"""

# A function to find  
def KSmallestUsingMorris(root, k): 
      
    # Count to iterate over elements  
    # till we get the kth smallest number  
    count = 0
  
    ksmall = -9999999999 # store the Kth smallest  
    curr = root # to store the current node  
  
    while curr != None: 
          
        # Like Morris traversal if current does 
        # not have left child rather than  
        # printing as we did in inorder, we  
        # will just increment the count as the  
        # number will be in an increasing order  
        if curr.left == None: 
            count += 1
  
            # if count is equal to K then we  
            # found the kth smallest, so store  
            # it in ksmall  
            if count == k:  
                ksmall = curr.key  
  
            # go to current's right child  
            curr = curr.right 
        else: 
              
            # we create links to Inorder Successor  
            # and count using these links  
            pre = curr.left  
            while (pre.right != None and 
                   pre.right != curr):  
                pre = pre.right  
  
            # building links  
            if pre.right == None: 
                  
                # link made to Inorder Successor  
                pre.right = curr  
                curr = curr.left 
  
            # While breaking the links in so made  
            # temporary threaded tree we will check  
            # for the K smallest condition  
            else: 
                  
                # Revert the changes made in if part  
                # (break link from the Inorder Successor)  
                pre.right = None
  
                count += 1
  
                # If count is equal to K then we  
                # found the kth smallest and so  
                # store it in ksmall  
                if count == k: 
                    ksmall = curr.key  
          
                curr = curr.right 
    return ksmall # return the found value
"""
TC = o(n)
SC = o(1)
"""