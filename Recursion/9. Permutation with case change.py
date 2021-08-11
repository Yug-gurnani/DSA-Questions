string = "abc"
ans = []
def solve(ip,op):
    global ans
    if len(ip) == 0:
        ans.append(op)
        return
    op1 = op
    op2 = op
    op1+= ip[0].upper()
    op2 += ip[0]
    ip = ip[1:]
    solve(ip,op1)
    solve(ip,op2)
    
    return
solve(string,"")
print(ans) 