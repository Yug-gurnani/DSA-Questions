s = "0100100111"
count0 = 0 
currmax0 = 0
count1 = 0
currmax1 = 0
for i in s:
    if i == "0":
        count0 += 1
        if count1 > 0:
            count0 -= 1
            count1 -= 1
        if currmax0 < count0:
            currmax0 = count0
    elif i == "1":
        count1 += 1
        if count0 > 0:
            count0 -= 1
            count1 -= 1
        if currmax1 < count1:
            currmax1 = count1
print(max(currmax1,currmax0))