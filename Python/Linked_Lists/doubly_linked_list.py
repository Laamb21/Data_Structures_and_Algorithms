#Doubly Linked List implementation 

import random

#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#Initialize Nodes with random integers
node1 = Node(random.randint(0,100))
node2 = Node(random.randint(0,100))
node3 = Node(random.randint(0,100))
node4 = Node(random.randint(0,100))
node5 = Node(random.randint(0,100))

#Link first node1 to node2
node1.next = node2

#Link node2 to node1 and node3 respectively
node2.prev = node1
node2.next = node3

#Link node3 to node2 and node4 respectively
node3.prev = node2
node3.next = node4

#Link node4 to node3 and node5 respectively
node4.prev = node3
node4.next = node5

#Link node5 to node4
node5.prev = node4

#Forward Traversal of Linked List
print("\nForward Traversal of Linked List:")
currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

#Backwards Traversal
print("\nBackwards Traversal of Linked List:")
currentNode = node5
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("null")