#Stack data structure implementation using linked lists

import random

#Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Stack class 
class Stack:
    #Initialization of stack
    def __init__(self):
        self.head = None
        self.size = 0

    #Push method
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    #Pop method
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    #Peek method
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    #isEmpty method
    def isEmpty(self):
        return self.size == 0
    
    #stackSize method
    def stackSize(self):
        return self.size
    

#Create a stack
stack = Stack()

#Push elements into stack, print using peek
stack.push(random.randint(0,10))
print("Push:",stack.peek())
stack.push(random.randint(0,10))
print("Push:",stack.peek())
stack.push(random.randint(0,10))
print("Push:",stack.peek())
stack.push(random.randint(0,10))
print("Push:",stack.peek())
stack.push(random.randint(0,10))
print("Push:",stack.peek())

#Pop method call
print("\nPop:",stack.pop())

#Peek method call
print("\nPeek:",stack.peek())

#isEmpty method call
print("\nisEmpty:",stack.isEmpty())

#stackSize method call
print("\nstackSize:",stack.stackSize())

    