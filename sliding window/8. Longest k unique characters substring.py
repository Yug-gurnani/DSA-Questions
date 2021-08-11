for _ in range(int(input())):
    s = input()
    k = int(input())
    i = 0
    j = 0
    dic = {}
    count = 0
    arr = [-1]
    n = len(s)
    while j < n:
        if s[j] not in dic:
            dic[s[j]] = 1
            count += 1
        else:
            dic[s[j]] += 1
        if count < k:
            j += 1
        elif count == k:
            arr.append(j-i+1)
            j += 1
        elif count > k:
            while count > k:
                dic[s[i]] -= 1
                if dic[s[i]] == 0:
                    del dic[s[i]]
                    count -= 1
                i += 1
            j += 1
    #print(n)
    #print(arr)
    print(max(arr))