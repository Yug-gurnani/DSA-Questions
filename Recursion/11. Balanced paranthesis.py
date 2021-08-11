n = 3
o = n
c = n
ans = []
def solve(o,c,op):
    global n
    global ans
    if o == 0 and c == 0:
        if len(op) == n*2:
            ans.append(op)
        return

    if o != 0:
        op1 = op
        op1 += "("
        solve(o-1,c,op1)
    if c > o:
        op2 = op
        op2 += ")"
        solve(o,c-1,op2)
    return
solve(o,c,"")
print(ans)