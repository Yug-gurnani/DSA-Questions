arr = []
for _ in range(int(input())):
    a,b = map(int,input().split())
    arr.append([a,b])
count = 0
arr.sort(key = lambda x:x[0],reverse = True)
arr.sort(key = lambda x: x[1],reverse=True)
count = 1
points = 0
for i in arr:
    if count > 0:
        points += i[0]
        count += i[1]
        count -= 1
    if count == 0:
        break
print(points) 
    
