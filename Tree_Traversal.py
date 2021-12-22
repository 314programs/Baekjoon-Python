class Node:
    def __init__ (self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

#root, left, right
def Preorder(node):
    print(node.data, end = "")
    if node.left_node != None:
        Preorder(Tree[node.left_node])
    if node.right_node != None:
        Preorder(Tree[node.right_node])

#left, root, right
def Inorder(node):
    if node.left_node != None:
        Inorder(Tree[node.left_node])
    print(node.data, end = "")
    if node.right_node != None:
        Inorder(Tree[node.right_node])

#left, right, root
def Postorder(node):
    if node.left_node != None:
        Postorder(Tree[node.left_node])
    if node.right_node != None:
        Postorder(Tree[node.right_node])
    print(node.data, end = "")
