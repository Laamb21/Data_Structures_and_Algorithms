#Binary Search Tree (BST) implementation

#Binary Tree Node class
class TreeNode: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Pre-order traversal function
def pre_order_traversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

#In-order traversal function
def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=", ")
    in_order_traversal(node.right)

#Post-order traversal function
def post_order_traversal(node):
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end=", ")

#Search function
def search(node, target):
    if node is None:
        return
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

#Insert function 
def insert(node, data):
    if node is None:
        return
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node


#Create nodes 
root = TreeNode(12)
node6 = TreeNode(6)
node4 = TreeNode(4)
node8 = TreeNode(8)
node14 = TreeNode(14)
node13 = TreeNode(13)
node20 = TreeNode(20)
node18 = TreeNode(18)

#Link nodes to form BST
root.left = node6
root.right = node14

node6.left = node4
node6.right = node8

node14.left = node13
node14.right = node20

node20.left = node18

#Pre-order traversal
print("\nPre-Order Traversal")
pre_order_traversal(root)
print()

#In-order traversal
print("\nIn-Order Traversal")
in_order_traversal(root)
print()

#Post-order traversal
print("\nPost-Order Traversal")
post_order_traversal(root)
print()

#Search for value
print("\nSearching for value 18...")
result = search(root, 18)
if result:
    print("Found node with value:",result.data)
else:
    print("Value not found")

#Insert new value
print("\nInserting new value: 2")
insert(root, 2)
print("In-Order Traversal with new node:")
in_order_traversal(root)