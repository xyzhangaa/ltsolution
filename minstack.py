###Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

###push(x) -- Push element x onto stack.
###pop() -- Removes the element on top of the stack.
###top() -- Get the top element.
###getMin() -- Retrieve the minimum element in the stack.    

def __init__(self):
    self.stack1 = []
    self.stack2 = []
def push(self, x):
    self.stack1.append(x)
    if len(self.stack2) == 0 or x <= self.stack2[-1]:
        self.stack2.append(x)

def pop(self):
    top = self.stack1[-1]
    self.stack1.pop()
    if top == self.stack2[-1]:
        self.stack2.pop()
        
def top(self):
    return self.stack1[-1]

def getMin(self):
    return self.stack2[-1]
