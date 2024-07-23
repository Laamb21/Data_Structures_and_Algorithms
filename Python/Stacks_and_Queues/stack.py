#Stack data structure implementation

import random

#Stack class
class Stack:
    #Initalization of stack
    def __init__(self):
        self.stack = []

    #Push method
    def push(self, element):
        self.stack.append(element)

    #Pop method
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    #Peek method
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    #isEmpty method
    def isEmpty(self):
        return len(self.stack) == 0
    
    #Size method
    def size(self):
        return len(self.stack)
    

#Create a stack
stack = Stack()

#Push elements into stack 
stack.push(random.randint(0,10))
stack.push(random.randint(0,10))
stack.push(random.randint(0,00))
stack.push(random.randint(0,10))
stack.push(random.randint(0,10))

#Print stack
print("\nStack:",stack.stack)

#Pop method call
print("\nPop:", stack.pop())

#Peek method call
print("\nPeek:",stack.peek())

#isEmpty method call
print("\nisEmpty:",stack.isEmpty())

#Size method call
print("\nSize:",stack.size())