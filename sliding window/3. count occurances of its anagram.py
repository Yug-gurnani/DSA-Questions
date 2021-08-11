def search(,pat, txt):
    dic = {}
    count = len(set(list(pat)))
    for i in pat:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1
    ans = 0
    k = len(pat)
    i = 0
    j = 0
    n = len(txt)
    while j < n:
        if txt[j] in dic:
            dic[txt[j]] -= 1
            if dic[txt[j]] == 0:
                count -= 1
        if j-i+1 < k:
            j += 1
        else:
            if count == 0:
                ans += 1
            if txt[i] in dic:
                if dic[txt[i]] == 0:
                    count += 1
                dic[txt[i]] += 1
            i += 1
            j += 1
    return ans