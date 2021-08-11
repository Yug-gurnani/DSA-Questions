"""
Your task  is to implement the function atoi.
The function takes a string(str) as argument and converts it to an integer and returns it.

Example 1:

Input:
str = 123
Output: 123
"""
def atoi(string):
    # Code here
    ans = 0
    flag = False
    for i in string:
        if ord(i) > 57:#to check if there is any characters
            return -1
        if i == "-":#to check the negative number
            flag = True
            continue
        ans = ans*10 + (ord(i) - ord("0"))
    if flag:
        return -ans
    return ans