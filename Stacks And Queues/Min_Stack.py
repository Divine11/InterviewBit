# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) – Push element x onto stack.
# pop() – Removes the element on top of the stack.
# top() – Get the top element.
# getMin() – Retrieve the minimum element in the stack.
# Note that all the operations have to be constant time operations.

# Questions to ask the interviewer :

# Q: What should getMin() do on empty stack? 
# A: In this case, return -1.

# Q: What should pop do on empty stack? 
# A: In this case, nothing. 

# Q: What should top() do on empty stack?
# A: In this case, return -1
#  NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor. 
class MinStack:

    def __init__(self):
        self.items = []
        self.min_stack = []

    def size(self):
        return len(self.items)

    # @param x, an integer
    def push(self, x):
        if self.size()==0:
            self.items.append(x)
            self.min_stack.append(x)
        else:
            current_min = self.min_stack[-1]
            if current_min<=x:
                self.min_stack.append(current_min)
            else:
                self.min_stack.append(x)
            self.items.append(x)

    # @return nothing
    def pop(self):
        if self.size()>0:
            self.items.pop()
            self.min_stack.pop()

    # @return an integer
    def top(self):
        if self.size()==0:
            return -1
        else:
            return self.items[-1]

    # @return an integer
    def getMin(self):
        if self.size()==0:
            return -1
        return self.min_stack[-1]

