def pattern(str, len):
    for i in range(0, len):
        revstr = str[::-1]
        j = len -1 - i
        for k in range(0, len):
         
            if (k == i):
                print(str[k],end = " ")
            elif (k == j):
                print(revstr[k], end = " ")
            else:
                print(end = " ")
         
        print(" ") 
pattern('siddharth',9)