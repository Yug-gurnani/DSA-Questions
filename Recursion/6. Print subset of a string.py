def to_string(a):
    res = ""
    for i in a:
        res += str(i)
    return res
def solve(ip,op,ans):
    if len(ip) == 0:
        ans.append(op)
        return 
    op1 = op[:]
    op2 = op[:]
    op2.append(ip[0])
    #print(op1,op2)
    ip = ip[1:]
    solve(ip,op1,ans)
    solve(ip,op2,ans)
    return
for _ in range(int(input())):
    n = int(input())
    ip = list(map(int,input().split()))
    ip.sort()
    op = []
    ans = []
    solve(ip,op,ans)
    #ans = list(set(ans))
    new = []
    for i in ans:
        if i not in new:
            new.append(i)
    for i in range(len(new)):
        new[i] = to_string(new[i])
    new.sort()
    for i in new:
        print("(",end = "")
        for j in range(len(i)):
            if j != len(i)-1:
                print(str(i[j]),end = " ")
            else:
                print(str(i[j]),end = "")
        print(")",end = "")
    print()