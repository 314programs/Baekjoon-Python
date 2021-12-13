class Node:
    def __init__ (self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def Preorder(node):
    print(node.data, end = "")
    if node.left_node != None:
        Preorder(Tree[node.left_node])
    if node.right_node != None:
        Preorder(Tree[node.right_node])

def Inorder(node):
    if node.left_node != None:
        Inorder(Tree[node.left_node])
    print(node.data, end = "")
    if node.right_node != None:
        Inorder(Tree[node.right_node])

def Postorder(node):
    if node.left_node != None:
        Postorder(Tree[node.left_node])
    if node.right_node != None:
        Postorder(Tree[node.right_node])
    print(node.data, end = "")
        
TreeSize = int(input())
Tree = {}

for i in range(TreeSize):
    data, left_node, right_node = input().split()
    if left_node == '.':
        left_node = None
    if right_node == '.':
        right_node = None
    Tree[data] = Node(data, left_node, right_node)

Preorder(Tree['A'])
print()
Inorder(Tree['A'])
print()
Postorder(Tree['A'])
