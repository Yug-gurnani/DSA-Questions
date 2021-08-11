"""
Implement a Stack using two queues q1 and q2.

Example 1:

Input:
push(2)
push(3)
pop()
push(4)
pop()
Output: 3 4
Explanation:
push(2) the stack will be {2}
push(3) the stack will be {2 3}
pop()   poped element will be 3 the 
        stack will be {2}
push(4) the stack will be {2 4}
pop()   poped element will be 4 
"""
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    queue_1.append(x)
    
def pop():
    '''
    :return: the value of top of stack and pop from it.
    '''
    global queue_1
    global queue_2
    if queue_1 == []:
        return -1
    else:
        while len(queue_1) > 1:
            temp = queue_1.pop(0)
            queue_2.append(temp)
        temp = queue_1.pop(0)
        while queue_2:
            queue_1.append(queue_2.pop(0))
        return temp
"""
TC = o(1) for push and o(n) for pop
SC = o(1) for both
"""