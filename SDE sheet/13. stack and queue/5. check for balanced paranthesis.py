"""
Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.

Example 1:

Input:
{([])}

Output: 
true

Explanation: 
{ ( [ ] ) }. Same colored brackets can form 
balaced pairs, with 0 number of 
unbalanced bracket.
"""
def mirror(i):
    if i == "]":
        return "["
    if i == ')':
        return "("
    if i == "}":
        return "{"
def ispar(x):
    op = {"{":1,"(":1,"[":1}
    cl = {"}":1,")":1,"]":1}
    stack = []
    x = list(x)
    for i in x:
        if i in cl:
            if not stack:
                return False
            if stack[-1] not in op:
                return False
            else:
                if stack[-1] != mirror(i):
                    return False
                else:
                    stack.pop()
        elif i in op:
            stack.append(i)
    if not stack:
        return True
"""
TC = o(n)
SC = o(n)
"""