def removeLoop(head):
    # code here
    # remove the loop without losing any nodes
    hare = head
    tort = head
    while tort:
        if (not hare or not hare.next or not hare.next.next):
            return
        tort = tort.next
        hare = hare.next.next
        if hare == tort:
            #print("loop h bhai")
            #print(hare.data)
            break

    else:
        return 0
        
    steps =0
    while True:
        tort = tort.next
        steps+=1
        if tort == hare:
            break
       
    hare = head
    tort = head
    for i in range(steps):
        hare = hare.next
    #print(steps)   
    while True:
        if hare == tort:
            break
        hare = hare.next
        tort = tort.next
        
    while True:
        if tort.next == hare:
            tort.next = None
            return head
        tort = tort.next