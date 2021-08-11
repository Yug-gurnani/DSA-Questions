"""
first row
last column
last row
first column
"""
def spirallyTraverse(a, r, c): 
    # code here 
    k = 0
    l = 0
    ans = []
    while k < r and l < c:
        for i in range(l,c):
            ans.append(a[k][i])
        k += 1
        for i in range(k,r):
            ans.append(a[i][c-1])
        c -= 1
        if k < r:
            for i in range(c-1,l-1,-1):
                ans.append(a[r-1][i])
            r -= 1
        if l < c:
            for i in range(r-1,k-1,-1):
                ans.append(a[i][l])
    
            l += 1
    return ans 