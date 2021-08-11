row, col = map(int, input().split(" "))

for i in range(row):
    pattern = "_|_"
    if i < (row-1)/2:
        print((pattern * (2*i+1)).center(col, "-"))
    elif i == (row-1)/2:
        print("WELCOME".center(col, "-"))
    else:
        print((pattern * (2*(row-1-i)+1)).center(col, "-"))