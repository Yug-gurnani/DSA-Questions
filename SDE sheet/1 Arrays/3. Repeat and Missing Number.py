"""
Given an unsorted array Arr of size N of positive integers.
One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array.
Find these two numbers.

N = 3
Arr[] = {1, 3, 3}
Output: 3 2
Explanation: Repeating number is 3 and 
smallest positive missing number is 2.
"""
#We use swap sort technique in this
def findTwoElement(arr, n): 
    for i in range(n):
        correct = arr[i] - 1
        while 1 <= arr[i] <= n and arr[i] != arr[correct]:
            arr[correct],arr[i] = arr[i],arr[correct]
            correct = arr[i]-1
    for i in range(n):
        if i + 1 != arr[i]:
            mis = i+1
            dup = arr[i]
    return [dup,mis]
"""
TC = O(n)
SC = O(1)
"""