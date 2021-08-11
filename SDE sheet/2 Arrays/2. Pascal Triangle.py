"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
#My method(by adding every two element of the last array)
def generate(self, n: int) -> List[List[int]]:
    
    if n == 0:
        return []
    ans = [[1]]
    for i in range(n-1):
        temp = ans[i]
        temp = temp
        new = [1]#because every new layer has 2 ones at the starting and end
        for i in range(len(temp)-1):
            temp1 = int(temp[i]) + int(temp[i+1])
            new.append(temp1)
        new.append(1) #because every new layer has 2 ones
        ans.append(new)
    return ans
#TC = O(n)
#SC = o(1) 
"""
If the question was given like this that given row and column number , give me the integer at that position in pascal triangle/
Then simply apply the NCR method
like if row = 4 and column = 3
you can compute like - (4*3*2) / (3*2*1)
the number of numbers on the numerator and denominator should remain same i.e if there are 3 numbers on the numerator there
will be 3 number in denominator.
TC= o(n) and SC = o(1)
"""

            