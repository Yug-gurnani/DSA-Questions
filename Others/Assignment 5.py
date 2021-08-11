"""
Q1. Write a Python program that accepts a string and calculate the number of digits and letters.
"""
S = input("Write a string to calculate the number of digits and letters \n")
digit = 0
letters = 0
for i in S:
    try:
        int(i)
        digit += 1
    except:
        letters+=1
print("No. of digits = {}".format(digit))
print("No. of letters = {}".format(letters))

"""
Q2. Write a Python program to check the validity of password input by users.
Validation Rules :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""
def check(s):
    symdic = {"$":1,"#":1,"@":1}
    low = False
    high = False
    num = False
    sym = False
    if len(s) < 6 or len(s) > 16:
        return False
    for i in s:
        try:
            int(i)
            num = True
        except:
            if i.islower():
                low = True
            if i.isupper():
                high = True
            if i in symdic:
                sym = True
    return low and high and num and sym

        
s = input("Write a string to check the validity of password input by user \n")
if check(s):
    print("Correct Pass")
else:
    print("Incorrect Pass")