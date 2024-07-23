#Singly Linked List implementation

import random

#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Function to find lowest value in a linked list
def find_lowest_value(node):
    min_value = node.data
    currNode = node.next
    while currNode:
        if currNode.data < min_value:
            min_value = currNode.data
        currNode = currNode.next
    return min_value


#Function to delete a node from a linked list
def delete_node(head, node_to_delete):
    if head == node_to_delete:
        return head.next
    
    currNode = head
    while currNode.next and currNode.next != node_to_delete:
        currNode = currNode.next
    
    if currNode.next is None:
        return head
    
    currNode.next = currNode.next.next

    return head

#Function to insert a node in a linked list
def insert_node(head, new_node, position):
    if position == 1:
        new_node.next = head
        return new_node
    
    currNode = head
    for _ in range(position - 2):
        if currNode is None:
            break
        currNode = currNode.next

    new_node.next = currNode.next
    currNode.next = new_node
    return head

#Initialize Nodes with random integers
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

#Initialize current Node
currentNode = node1

#Print Linked List
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

#Print lowest value 
print("\nLowest value in linked list:",find_lowest_value(node1))

#Delete a node
node1 = delete_node(node1, node3)
print("\nList after deleting Node 3:")
currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

#Replace deleted node with a new node 
newNode = Node(random.randint(0,100))
node1 = insert_node(node1, newNode, 3)
print("\nList after inserting new node at position 3:")
currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")