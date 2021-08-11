def intersetPoint(head_a,head_b):
    #code
    c1 = 0
    c2 = 0
    temp = head_a
    while temp:
        c1 += 1
        temp = temp.next
        
    temp = head_b
    while temp:
        c2 += 1
        temp = temp.next
    c3 = abs(c1-c2)
    c4 = c3
    if c1 > c2:
        temp = head_a
        while c3 != 0:
            temp = temp.next
            c3 -= 1
        temb = head_b
        while temp:
            if temp == temb:
                return temp.data
            else:
                temp = temp.next
                temb = temb.next
    if c1 < c2:
        temp = head_b
        while c4 != 0:
            temp = temp.next
            c4 -= 1
        temb = head_a
        while temp:
            
            if temp == temb:
                return temp.data
            else:
                temp = temp.next
                temb = temb.next
    if c1 == c2:
        temp = head_a
        temb = head_b
        while temp:
            
            if temp == temb:
                return temp.data
            else:
                temp = temp.next
                temb = temb.next
        
                
    return -1