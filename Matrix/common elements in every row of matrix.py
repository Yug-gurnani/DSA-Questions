mat = [[1,2,1,4,8],[3,7,8,5,1],[8,7,7,3,1],[8,1,2,7,9]]
n = len(mat)
m = len(mat[0])
dic = {}
for i in range(n):
    for j in range(m):
        if mat[i][j] not in dic:
            dic[mat[i][j]] = [1,i]
        else:
            if dic[mat[i][j]][1] == i:
                pass
            else:
                dic[mat[i][j]][0] += 1
                dic[mat[i][j]][1] = i
#print(dic,m)
for i in dic:
    if dic[i][0] == n:
        print(i)
