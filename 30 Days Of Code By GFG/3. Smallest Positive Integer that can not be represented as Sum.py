"""
Given an array of size N, find the smallest positive integer value that cannot be represented as sum of some elements from the array.


Example 1:

Input: 
N = 6
array[] = {1, 10, 3, 11, 6, 15}
Output: 
2
Explanation:
2 is the smallest integer value that cannot 
be represented as sum of elements from the array.




array = [1,10,4,9,2]
sorted array = [1,2,4,9,10]

initially next_unreachable_number = 1
[1,2,4,9,10] -> i = 1 -> 1<= 1, therefore next_unreachable_number = 1+1 = 2
[1,2,4,9,10] -> i = 2 -> 2<= 2, therefore next_unreachable_number = 2+2 = 4
[1,2,4,9,10] -> i = 4 -> 4<= 4, therefore next_unreachable_number = 4+4 = 8
[1,2,4,9,10] -> i = 9 -> 9<= 8, hence return next_unreachable_number = 8

so the logic is next unreachable number is one plus than current number we are pointing to in array
"""
def smallestpositive(self, arr, n):  
    arr.sort()
    res = 1
    i = 0
    while i < n and arr[i] <= res:
        res += arr[i]
        i += 1
    return res
"""
TC = o(n log n)
SC = o(1)
"""
