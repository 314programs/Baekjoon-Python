from collections import deque
import sys
input = sys.stdin.readline

#Input nodes into the dictionary
Nodes = int(input())
NodeDict = {}

for i in range(1, Nodes+1):
    NodeDict[i] = []
for i in range(Nodes-1):
    Parent, Child = map(int, input().split())
    NodeDict[Parent].append(Child)
    NodeDict[Child].append(Parent)
    
Visited = [0]*Nodes
queue = deque([1])

#BFS
while queue:
    Temp = queue.popleft()
    
    for item in NodeDict[Temp]:
        if Visited[item-1] == 0:
            Visited[item-1] = Temp
            queue.append(item)

for i in range(1,Nodes):
    sys.stdout.write(str(Visited[i])+'\n')
