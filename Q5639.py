import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

#Node class
class Node:
    def __init__ (self, left_node, right_node):
        self.left_node = left_node
        self.right_node = right_node
        
#Post order function
def Postorder(node):
    if Tree[node].left_node != None:
        Postorder(Tree[node].left_node)
    if Tree[node].right_node != None:
        Postorder(Tree[node].right_node)
    print(node)

#Make a tree using dictionary to post order
def MakeTree(root, node):
    if node < root:
        if Tree[root].left_node == None:
            Tree[root].left_node = node
        else:
            MakeTree(Tree[root].left_node, node)
    
    if node > root:
        if Tree[root].right_node == None:
            Tree[root].right_node = node
        else:
            MakeTree(Tree[root].right_node, node)
    
    if node == root:
        return
    
Tree = {}
NodeList = []

#Get input
while True:
    try:
        num = int(input())
        NodeList.append(num)
        Tree[num] = Node(None, None)
        MakeTree(NodeList[0], num)
    except:
        break
    
    
Postorder(NodeList[0])
