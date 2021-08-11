def reverse(head, k):
    # Code here
    curr = head
    next = None
    prev = None
    count = 0
    while curr and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
    
    if next:
        head.next = reverse(next,k)
    return prev