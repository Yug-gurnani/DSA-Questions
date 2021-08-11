class Stack():
    def __init__(self,size):
        self.size = size
        self.stack = []
        self.top = 0
        
    def push(self,elem):
        if self.top == self.size - 1:
            print('stack_overflow')
        else:
            self.stack.append(elem)
            self.top +=1
    
    def pop(self):
        if self.top == 0:
            print('underflow')
            return
        else:
            value = self.stack.pop()
            self.top-=1
            print(value)
            return
    
    def peek(self):
        if self.top==0:
            print('stack is empty')
            return
        print(self.stack[self.top-1])
        return
    
c = Stack(5)

c.push(2)
c.push(9)
c.push(10)
c.pop()
c.peek()
print(c.stack)
c.pop()
c.pop()
c.peek()
c.push(2)
c.push(9)
c.push(10)
print(c.stack)