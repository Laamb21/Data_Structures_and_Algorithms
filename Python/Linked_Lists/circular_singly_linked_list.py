#Circular Singly Linked List implementation 

import random

#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Initialize Node with random integers
node1 = Node(random.randint(0,100))
node2 = Node(random.randint(0,100))
node3 = Node(random.randint(0,100))
node4 = Node(random.randint(0,100))
node5 = Node(random.randint(0,100))

#Link Nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#Initialize currentNode and startNode
currentNode = node1
startNode = node1

#Print first node
print(currentNode.data, end=' -> ')
currentNode = currentNode.next

#Print rest of Linked List
while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("...")