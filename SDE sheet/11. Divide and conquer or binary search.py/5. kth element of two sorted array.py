"""
Given two sorted arrays A and B of size M and N respectively and an element k.
The task is to find the element that would be at the k’th position of the final sorted array.
"""
for _ in range(int(input())):
    n,m,k = map(int,input().split())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    i = 0
    j = 0
    k_f = 0
    while i < n and j < m:
        if arr[i] < brr[j]:
            k_f += 1
            if k_f == k:
                print(arr[i])
            i += 1
        else:
            k_f += 1
            if k_f == k:
                print(brr[j])
            j += 1
    while i < n and k_f < k:
        k_f += 1
        if k == k_f:
            print(arr[i])
        i += 1
    while j < m and k_f < k:
        k_f += 1
        if k == k_f:
            print(brr[j])
        j += 1
"""
TC = o(k)
SC = o(1)
"""