"""
Given an array of integers arr[] and a number m,
count the number of subarrays having XOR of their elements as m.

Input : arr[] = {4, 2, 2, 6, 4}, m = 6
Output : 4
Explanation : The subarrays having XOR of 
              their elements as 6 are {4, 2}, 
              {4, 2, 2, 6, 4}, {2, 2, 6},
               and {6}

An Efficient Solution solves the above problem in O(n) time. 
Let us call the XOR of all elements in the range [i+1, j] as A,
in the range [0, i] as B, and in the range [0, j] as C. 
If we do XOR of B with C, the overlapping elements in [0, i] from B and C zero out, 
and we get XOR of all elements in the range [i+1, j], i.e. A.
Since A = B XOR C, we have B = A XOR C. Now, if we know the value of C and we take the value of A as m,
we get the count of A as the count of all B satisfying this relation.
Essentially, we get the count of all subarrays having XOR-sum m for each C.
As we take the sum of this count overall C, we get our answer.

Its solution is based on largest subarray with 0 sum
"""
def subarrayxor(arr,n,m):
    ans = 0
    dic = {}
    xor = 0
    for i in range(n):
        xor = xor ^ arr[i]
        if xor == m:
            ans += 1
        if xor^m in dic:
            ans += dic[xor^m]
        if xor not in dic:
            dic[xor] = 1
        else:
            dic[xor] += 1
    return ans
"""
arr = [4,2,2,6,4]
n = 5
m = 6
print(subarrayxor(arr,n,m))
"""
"""
TC = o(n)
SC = o(n)
"""