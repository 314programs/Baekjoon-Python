import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

#Node setup
class Node:
    def __init__ (self, left_node, right_node, root):
        self.left_node = left_node
        self.right_node = right_node 
        self.root = root

Node_Num = int(input())
Node_List = [Node(-1, -1, -1) for v in range(Node_Num + 1)]
First_root = 1

Max_length = 0
Max_depth = 0

for i in range(Node_Num):
    self_, left_, right_ = map(int, input().split())
    Node_List[self_].left_node = left_
    Node_List[self_].right_node = right_
    #Got confused here because if left_ or right_ was -1 it would go to end of the list...
    if left_ != -1: Node_List[left_].root = self_
    if right_ != -1: Node_List[right_].root = self_

for i in range(1, Node_Num+1):
    if Node_List[i].root == -1:
        First_root = i

Depth_graph = [[] for v in range(Node_Num + 1)]

index = 1

#Preorder
def DFS(start, depth):
    global index
    if Node_List[start].left_node != -1:
        DFS(Node_List[start].left_node, depth + 1)
    
    #Compare how far to the right it is using index
    Depth_graph[depth].append(index)
    index += 1
    
    if Node_List[start].right_node != -1:
        DFS(Node_List[start].right_node, depth + 1)

DFS(First_root, 1)

#Calculate max length by going through each non empty depth
for i in range(1, Node_Num+1):
    if Depth_graph[i] == []:
        break
    else:
        if Max_length < max(Depth_graph[i]) - min(Depth_graph[i]) + 1:
            Max_length = max(Depth_graph[i]) - min(Depth_graph[i]) + 1
            Max_depth = i

print(Max_depth, Max_length)
