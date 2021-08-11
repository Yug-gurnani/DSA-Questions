def solve(s,i,j,ans,istrue,dp_map):
    temp = str(i) + " " + str(j) + " " + str(istrue)
    if temp in dp_map:
        return dp_map[temp]
    if  i > j:
        return 0
    if i == j:
        if istrue:
            if s[i] == "T":
                dp_map[temp] = 1
                return dp_map[temp]
            else:
                dp_map[temp] = 0
                return dp_map[temp]
        else:
            if s[i] == "F":
                dp_map[temp] = 1
                return dp_map[temp]
            else:
                dp_map[temp] = 0
                return dp_map[temp]
    ans = 0
    for k in range(i+1,j,2):
        lt = solve(s,i,k-1,ans,True,dp_map)
        lf = solve(s,i,k-1,ans,False,dp_map)
        rt = solve(s,k+1,j,ans,True,dp_map)
        rf = solve(s,k+1,j,ans,False,dp_map)
        if s[k] == "&":
            if istrue:
                ans += lt * rt
            else:
                ans += lf * rf + lt  * rf + lf * rt 
        elif s[k] == "|":
            if istrue:
                ans += lt * rt + lf * rt + lt * rf
            else:
                ans += lf * rf
        elif s[k] == "^":
            if istrue:
                ans += lt * rf + rt * lf
            else:
                ans += lt * rt + lf * rf
        
    dp_map[temp] = ans
    return dp_map[temp]
dp_map = {}
print(solve("T|T&F^T",0,6,0,True,dp_map))
