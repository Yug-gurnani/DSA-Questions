#3.1
print("Pattern 1")
for i in range(1,7):
    print("*"*i)
print("-----------------------------------")
#3.2
print("Pattern 2")
for i in range(7,0,-1):
    print("*"*i)
print("-----------------------------------")
#3.3
print("Pattern 3")
max =7
for i in range(-7,0,1):
    if abs(i) == max:
        print("*"*abs(i))
    elif abs(i) == max-6:
        print("*")
    else:
       print("*"+" "*abs(i+1)+"*")
print("-----------------------------------")
#3.4
print("Pattern 4")
k=5
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")
print("-----------------------------------")
#3.5
print("Pattern 5")
for rows in range(6, 0, -1):
    for columns in range(0, 6-rows):
        print(end=" ")
    for columns in range(0, rows):
        print("*", end=" ")
    print()
print("-----------------------------------")
#3.6
print("Pattern 6")
for i in range(6):
    for j in range(6-i):
        print(' ', end=' ')
    
    for j in range(2*i+1):
        if j==0 or j==2*i or i==6-1:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print()