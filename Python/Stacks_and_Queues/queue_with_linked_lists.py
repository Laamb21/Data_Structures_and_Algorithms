#Queue data structure implementation using linked lists

import random

#Node class
class Node:
    #Initialization of node
    def __init__(self, data):
        self.data = data
        self.next = None

#Queue class
class Queue:
    #Initialization of queue 
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    #Enqueue method
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    #Dequeue method
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    #Peek method
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    #isEmpty method
    def isEmpty(self):
        return self.length == 0
    
    #Size method 
    def size(self):
        return self.length
    
    #printQueue method
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


#Create a queue
queue = Queue()

#Enqueue elements into queue
queue.enqueue(random.randint(0,10))
queue.enqueue(random.randint(0,10))
queue.enqueue(random.randint(0,10))
queue.enqueue(random.randint(0,10))
queue.enqueue(random.randint(0,10))

#Print queue
print("\nQueue:", end=" ")
queue.printQueue()

#Dequeue method call
print("\nDequeue:", queue.dequeue())

#Peek method call
print("\nPeek:", queue.peek())

#isEmpty method call
print("\nisEmpty:", queue.isEmpty())

#Size method call
print("\nSize:", queue.size())