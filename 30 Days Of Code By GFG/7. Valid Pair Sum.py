"""
Given an array of size N, find the number of distinct pairs {a[i], a[j]} (i != j) in the array with their sum greater than 0.

Example 1:

Input: N = 3, a[] = {3, -2, 1}
Output: 2
Explanation: {3, -2}, {3, 1} are two 
possible pairs.
"""
def ValidPair(self, a, n): 
    	# Your code goes here
    	a.sort()
    	
    	
    	#print(a)
    	i = 0
    	j = n-1
    	count = 0
    	while i < j:
    	    
    	    #print(a[i],a[j])
    	    if a[i] == None:
    	        i += 1
    	        continue
    	    if a[j] == None:
    	        j-=1
    	        continue
    	    if a[i] + a[j] > 0:
    	        count += j-i
    	        j -= 1
    	    else:
    	        i += 1
    	return count
"""
TC = o(n log n)
SC = o(1)
"""
