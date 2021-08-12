"""
https://www.interviewbit.com/problems/subarray-with-given-xor/
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, a, b):
        dic = {}
        ans = 0
        xor = 0
        for i in a:
            xor = xor ^ i

            y = xor ^ b

            if xor == b:
                ans += 1
            if y in dic:
                ans += dic[y]
            if xor in dic:
                dic[xor] += 1
            else:
                dic[xor] = 1
        return ans