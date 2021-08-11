"""
Geek and his classmates change their Position when the teacher turns her back

So the student with roll number x sitting on desk number i replaces his position with the person of roll number i

determine the next position of all the students

Modify the array in place

So the formula is :
Let one student be a and second b
if a is set to a + b * n
the a // n will be b
eg: a = 3 b = 4 n = 5
a = 3 + 4 * 5
then a // n = 23 // 5 = 4 == b
"""
def solve(arr,n):

    for i in range(n):
        arr[i] = arr[i] + (arr[arr[i]]%n)*n
    for i in range(n):
        arr[i] = arr[i] // n
"""
TC = o(n)
SC = o(1)
"""