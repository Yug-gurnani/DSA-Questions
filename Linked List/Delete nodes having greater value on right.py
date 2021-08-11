def reverse(head):
    if not head.next:
        return head
    l = None
    m = head
    r = head
    while m:
        r = m.next
        m.next = l
        l = m
        m = r
        
    return l
    
def compute(head):
    
    rhead = reverse(head)
    mx = rhead.data
    mhead = rhead
    temp = rhead.next
    while temp:
        if temp.data >= rhead.data:
            rhead.next = temp
            rhead = temp
            
        temp = temp.next
    rhead.next = None 
    return reverse(mhead)