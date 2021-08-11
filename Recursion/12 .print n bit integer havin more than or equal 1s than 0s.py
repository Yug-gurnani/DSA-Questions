def solve(o,z,n,op):
    if n == 0:
        print(op)
        return
    if o > z:
        z += 1
        op2 = op
        op2 += "0"
        solve(o,z,n-1,op2)
    op1 = op
    op1 += "1"
    o += 1
    solve(o,z,n-1,op1)
    
n = 4
ones = 0
zeros = 0
solve(ones,zeros,n,"")