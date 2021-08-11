def letterCasePermutation(S):
        ans = []
        def solve(ip,op):
            nonlocal ans
            if len(ip) == 0:
                ans.append(op)
                return
            op1 = op
            op2 = op
            if ip[0].isupper():
                op1 += ip[0].lower()
            else:
                op1 += ip[0].upper()
            op2 += ip[0]
            ip = ip[1:]
            solve(ip,op1)
            solve(ip,op2)
            return
        solve(S,"")
        return list(set(ans))
        