#Queue data structure implementation

import random

#Queue class
class Queue:
    #Initialization of queue
    def __init__(self):
        self.queue = []

    #Enqueue method
    def enqueue(self, element):
        self.queue.append(element)

    #Dequeue mehtod
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    #Peek method
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    #isEmpty method
    def isEmpty(self):
        return len(self.queue) == 0
    
    #Size method
    def size(self):
        return len(self.queue)
    

#Create a queue 
queue = Queue()

#Enqueue elements into queue
queue.enqueue(random.randint(0,10))
queue.enqueue(random.randint(0,10))
queue.enqueue(random.randint(0,10))
queue.enqueue(random.randint(0,10))
queue.enqueue(random.randint(0,10))

#Print queue
print("\nQueue:",queue.queue)

#Dequeue method call
print("\nDequeue:",queue.dequeue())

#Peek method call
print("\nPeek",queue.peek())

#isEmpty method call
print("\nisEmpty:",queue.isEmpty())

#Size method call
print("\nSize:",queue.size())