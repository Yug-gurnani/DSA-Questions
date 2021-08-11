"""
Geek Land has a population of N people and each person's ability to rule the town is measured by a numeric value arr[i].
The two people that can together rule Geek Land must be compatible with each other i.e.,
the sum of digits of their ability arr[i] must be equal. Their combined ability should be maximum amongst all the
possible pairs of people. Find the combined ability of the Ruling Pair.

Example 1:

Input:
N = 5
arr[] = {55, 23, 32, 46, 88}
Output:
101
Explanation:
All possible pairs that are 
compatible with each other are- (23, 32) 
with digit sum 5 and (55, 46) with digit 
sum 10. Out of these the maximum combined 
ability pair is (55, 46) i.e. 55 + 46 = 101
"""
def RulingPair(self, arr, n): 
    	# Your code goes here
    dic = {}
    mx = 0
    for i in range(n):
        tmp = arr[i]
        s = 0
        while tmp:
            s += tmp%10
            tmp = tmp//10
        if s in dic:
            mx = max(dic[s]+arr[i],mx)
        
            dic[s] = max(arr[i],dic[s])
        else:
            dic[s] = arr[i]
    if mx == 0:
        return -1
    return mx
"""
TC = o(n)
SC = o(n)
"""