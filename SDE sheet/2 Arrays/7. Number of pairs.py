"""
Given two arrays X and Y of positive integers,
find the number of pairs such that xy > yx (raised to power of) where x is an element from X and y is an element from Y.

Example 1:

Input: 
M = 3, X[] = [2 1 6] 
N = 2, Y[] = [1 5]
Output: 3
Explanation: 
The pairs which follow xy > yx are 
as such: 21 > 12,  25 > 52 and 61 > 16 


Following are simple steps based on this trick.  

Sort array Y[].
For every x in X[], find the index idx of smallest number greater than x (also called ceil of x) in Y[] using binary search or we can use the inbuilt function upper_bound() in algorithm library.
All the numbers after idx satisfy the relation so just add (n-idx) to the count.
Base Cases and Exceptions: 
Following are exceptions for x from X[] and y from Y[]  

If x = 0, then the count of pairs for this x is 0.
If x = 1, then the count of pairs for this x is equal to count of 0s in Y[].
x smaller than y means x^y is greater than y^x.
x = 2, y = 3 or 4
x = 3, y = 2
"""
import bisect
def solve(x,Y,n,countarr):
    if x == 0:
        return 0
    if x == 1:
        return countarr[0]
    idx = bisect.bisect_right(Y,x)
    ans = n - idx
    ans += countarr[0] + countarr[1]
    
    if x == 2:
        ans -= countarr[3] + countarr[4]
    
    if x == 3:
        ans += countarr[2]
    return ans
def countPairs(a,b,m,n):
    #code here
    countarr = [0] * 5
    for i in b:
        if i < 5:
            countarr[i] += 1
    b.sort()
    ans = 0
    for i in a:
        ans += solve(i,b,n,countarr)
    return ans
"""
TC = o((n+m)*log(n))
SC = o(1)
"""
