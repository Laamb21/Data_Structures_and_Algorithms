#Binary Tree implementation 

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


#Create nodes
root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')
nodeH = TreeNode('H')
nodeI = TreeNode('I')
nodeJ = TreeNode('J')
nodeK = TreeNode('K')
nodeL = TreeNode('L')
nodeM = TreeNode('M')
nodeN = TreeNode('N')

#Link nodes to form tree
root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeC.left = nodeG
nodeC.right = nodeH

nodeD.left = nodeI
nodeD.right = nodeJ

nodeE.left = nodeK
nodeE.right = nodeL

nodeF.left = nodeM
nodeF.right = nodeN

#Pre-order traversal 
print("\nPre-Order Traversal")
pre_order_traversal(root)

#In-order traversal
print("\nIn-Order Traversal")
in_order_traversal(root)

#Post-order traversal
print("\nPost-Order Traversal")
post_order_traversal(root)