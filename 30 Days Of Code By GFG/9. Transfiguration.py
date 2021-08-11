"""
Professor McGonagall teaches transfiguration at Hogwarts.
She has given Harry the task of changing himself into a cat.
She explains that the trick is to analyze your own DNA and change it into the DNA of a cat.
The transfigure spell can be used to pick any one character from the DNA string, remove it and insert it in the beginning. 
Help Harry calculates minimum number of times he needs to use the spell to change himself into a cat.

Example 1:

Input: 
A = "GEEKSFORGEEKS" 
B = "FORGEEKSGEEKS"
Output: 3
Explanation:The conversion can take place 
in 3 operations:
1. Pick 'R' and place it at the front, 
   A="RGEEKSFOGEEKS"
2. Pick 'O' and place it at the front, 
   A="ORGEEKSFGEEKS"
3. Pick 'F' and place it at the front, 
   A="FORGEEKSGEEKS

Start matching from last characters of both strings. If last characters match,
then our task reduces to remaining characters. If last characters don’t match,
then find the position of B’s mismatching character in A.
The difference between two positions indicates that these many characters of A must be moved.
"""
def transfigure(self, a, b): 
    dic1 = {}
    dic2 = {}
    for i in range(len(a)):
        if a[i] not in dic1:
            dic1[a[i]] = 0
        if b[i] not in dic2:
            dic2[b[i]] = 0
        dic1[a[i]] += 1
        dic2[b[i]] += 1
    if len(a)!=len(b):
        return -1
    elif dic1 != dic2:
        return -1
        
    else:
        n = len(a)
        count = 0
        i = n-1
        j = n-1
        while i >= 0 and j >= 0:
            if a[i] != b[j]:
                while i >= 0 and b[j] != a[i]:
                    count += 1
                    i -= 1
            else:
                i -= 1
                j -= 1
            
            
            
        return count