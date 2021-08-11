"""
Geek wants to make a special space for candies on his bookshelf. Currently,
it has N books of different heights and unit width. Help him select 2 books such
that he can store maximum candies between them by removing all the other books from between the selected books. The task is to
find out the area between 2 books that can hold the maximum candies without changing the original position of selected books. 


Input: N = 6, height[] = {2, 1, 3, 4, 6, 5}
Output: 8
Explanation: We remove the 4 books in the middle 
creating length = 4 for the candy dam. Height 
for dam will be min(2,5) = 2. Area between book 
of height 2 and book of height 5 is 2 x 4 = 8.
"""
def maxCandy(self, height, n): 
    i = 0
    j = n-1
    mx = 0
    while i < j:
        area = (j-i-1) * min(height[i],height[j])
        mx = max(area,mx)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return mx
"""
TC = o(n)
SC = o(1)
"""