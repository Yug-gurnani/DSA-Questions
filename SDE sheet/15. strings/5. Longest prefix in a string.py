"""
Given a array of N strings, find the longest common prefix among all strings present in the array.

Example 1:

Input:
N = 4
arr[] = {geeksforgeeks, geeks, geek,
         geezer}
Output: gee
Explanation: "gee" is the longest common
prefix in all the given strings.
"""
def longestCommonPrefix(self, arr, n):
    m = len(arr[0])
    ans = ""
    for i in range(n):
        m = min(m,len(arr[i]))
    for i in range(m):
        curr = arr[0][i]
        for j in range(1,n):
            if curr != arr[j][i]:
                if ans == "":
                    return -1
                return ans
        ans += arr[0][i]
    if ans == "":
        return -1
    return ans
"""
TC = o(n*len of shortest string)
SC = o(1)
"""