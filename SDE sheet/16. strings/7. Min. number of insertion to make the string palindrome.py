"""
Given a string str we need to tell minimum characters to be added at front of string to make string palindrome.

Examples:

Input  : str = "ABC"
Output : 2
We can make above string palindrome as "CBABC"
by adding 'B' and 'C' at front.

Input  : str = "AACECAAAA";
Output : 2
We can make above string palindrome as AAAACECAAAA
by adding two A's at front of string.

Efficient approach: We can solve this problem efficiently in O(n) time using lps array of KMP algorithm.
First we concat string by concatenating given string, a special character and reverse of given string then we will get lps array for this concatenated string,
recall that each index of lps array represent longest proper prefix which is also suffix. We can use this lps array for solving the problem.

For string = AACECAAAA
Concatenated String = AACECAAAA$AAAACECAA
LPS array will be {0, 1, 0, 0, 0, 1, 2, 2, 2, 
                   0, 1, 2, 2, 2, 3, 4, 5, 6, 7}
Here we are only interested in the last value of this lps array because it shows us the largest suffix of the reversed string that matches the prefix of the original string i.e these many characters already satisfy the palindrome property.
Finally minimum number of character needed to make the string a palindrome is length of the input string minus last entry of our lps array. Pease see below code for better understanding
"""
def solve(s):
    m = len(s)
    s = s + "$" + s[::-1]
    n = len(s)
    i = 1
    j = 0
    lps = [0] * n
    while i < n:
        if s[i] == s[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return m - lps[-1]
"""
TC = o(n)
SC = o(n)
"""
