"""
There are N buildings in Linear Land. They appear in a linear line one after the other and their
heights are given in the array arr[]. Geek wants to select three buildings in Linear Land and remodel
them as recreational spots. The third of the selected building must be taller than the first and shorter than the second.
Can geek build the three-building recreational zone? 


Example 1:

Input:
N = 6
arr[] = {4, 7, 11, 5, 13, 2}
Output:
True
Explanation:
[4, 7, 5] fits the condition.
"""
def recreationalSpot(self, arr, n):
    # Your code goes here 
    currmin = currmax = arr[0]
    if n < 3:
        return False
    for i in range(1,n):
        if arr[i] < currmin:
            currmin = arr[i]
        if arr[i] > currmax:
            currmax = arr[i]
        if arr[i] > currmin and arr[i] < currmax:
            return True
    return False
"""
TC = o(n)
SC = o(1)
"""