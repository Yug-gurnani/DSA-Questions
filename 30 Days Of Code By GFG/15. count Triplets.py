"""
Given a sorted linked list of distinct nodes (no two nodes have the same data) and an integer X.
Count distinct triplets in the list that sum up to given integer X.

Example 1:

Input: LinkedList: 1->2->4->5->6->8->9, X = 17
Output: 2
Explanation: Distinct triplets are (2, 6, 9) 
and (4, 5, 8) which have sum equal to X i.e 17.
"""
def lltoarray(head,arr):
    tmp = head
    while tmp:
        arr.append(tmp.val)
        tmp = tmp.nxt
    return arr
def countTriplets(head,x):
    arr = lltoarray(head,[])
    n = len(arr)
    count = 0
    arr.sort()
    for i in range(n-2):
        j = i+1
        k = n-1
        while j < k:
            s = arr[i] + arr[j] + arr[k]
            if s == x:
                count += 1
                j += 1
            elif s < x:
                j += 1
            else:
                k -= 1
    return count
"""
TC = o(n^2)
SC = o(n)
"""