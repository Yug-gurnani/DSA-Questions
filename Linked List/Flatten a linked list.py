def merge(a,b):
    if a == None:
        return b
    if b == None:
        return a
        
        
    result = None
    
    if a.data < b.data:
        result = a
        result.bsottom = merge(a.bottom,b)
    else:
        result = b
        result.bottom = merge(a,b.bottom)
    return result
def flatten(root):
    #Your code here
    if root == None or root.next == None:
        return root
    return merge(root,flatten(root.next))