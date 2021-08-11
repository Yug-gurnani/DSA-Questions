n = 4
k = 5
def compliment(i):
    if i == 0:
        return 1
    else:
        return 0
def solve(n,k):
    if n == 1 and k == 1:
        return 0
    mid = (2**(n-1))//2
    if k <= mid:
        return solve(n-1,k)
    else:
        return compliment(solve(n-1,k-mid))
print(solve(n,k))