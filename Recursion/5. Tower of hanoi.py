n = 3
s = 1
h = 2
d = 3
count = [0]
def solve(s,d,h,n,count):
    if n == 1:
        print("Moving plate {} from {} to {}".format(n,s,d))
        count[0] += 1
        return 
    solve(s,h,d,n-1,count)
    count[0] += 1
    print("Moving plate {} from {} to {}".format(n,s,d))
    solve(h,d,s,n-1,count)
    return
solve(s,h,d,n,count) 
print(count[0])