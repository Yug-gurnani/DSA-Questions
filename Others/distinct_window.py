def first(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
    distinct = s
    temps = s
    #print(dic)
    for i in range(len(temps)):
        if dic[temps[i]] > 1:
            dic[temps[i]] -= 1
            distinct = temps[i+1:]
        else:
            break
    temps = distinct
    temps = temps[::-1]
    for i in range(len(temps)):
        if dic[temps[i]] > 1:
            dic[temps[i]] -= 1
            distinct = temps[i+1:]
        else:
            break
    print(dic)
    return distinct
def second(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
    temps = s[::-1]
    distinct = s[::-1]
    #print(dic)
    for i in range(len(temps)):
        if dic[temps[i]] > 1:
            dic[temps[i]] -= 1
            distinct = temps[i+1:]
        else:
            break
    temps = distinct
    temps = temps[::-1]
    for i in range(len(temps)):
        if dic[temps[i]] > 1:
            dic[temps[i]] -= 1
            distinct = temps[i+1:]
        else:
            break
    print(dic)
    return distinct
    
    
    
    
for _ in range(int(input())):
    s = input()
    dic = {}
    
    a = first(s)
    b =second(s)
    print(len(s))

    print(a)
    print(b)
    print(min(len(a),len(b)))

    
    