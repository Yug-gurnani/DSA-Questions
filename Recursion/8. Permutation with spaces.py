def solve(ip,op,n):
    global ans
    if len(ip) == 0:
        if len(op) >= n: 
            ans.append(op)
        return
    op1 = op
    op2 = op
    op1 += ip[0]
    op1 += " "
    op2 += ip[0]
    ip = ip[1:]
    solve(ip,op1,n)
    solve(ip,op2,n)
    return
for _ in range(int(input())):
    s = input()
    ans = []
    solve(s,"",len(s))
    for i in range(len(ans)):
        if ans[i][-1] == " ":
            ans[i] = ans[i][:-1]
    ans = sorted(list(set(ans)))
    for i in ans:
        print("(",end = "")
        for j in range(len(i)):
            if j != len(i)-1:
                print(i[j],end = "")
            else:
                print(i[j],end = "")
        print(")",end = "")
    print()
            