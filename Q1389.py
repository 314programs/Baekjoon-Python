from collections import deque
import sys

#Set up dictionary for connections
People, Connections = map(int, input().split())
ConnectionList = []
ConnectionDict = {}

for i in range(Connections):
    ConnectionList.append(list(map(int, input().split())))

for i in range(1, People+1):
    ConnectionDict[i] = []
    
for item in ConnectionList:
    ConnectionDict[item[0]].append(item[1])
    ConnectionDict[item[1]].append(item[0])
    
ResultList = []

#Use BFS to calculate the connections, add +1 depth everytime to calculate the distance
def BFS(Start, Q, depth):
    queue = Q
    Store = []
    
    for thing in queue:
        for item in ConnectionDict[thing]:
            if item not in Visited:
                Visited.append(item)
                Store.append(item)

    for a in Store:
        Result.append(depth)
        BFS(item, Store, depth + 1)
            
Answer = []

#Print the smallest value's index + 1
for i in range(1, People+1):
    TempQ = [i]
    Visited = [i]
    Result = []
    BFS(i, TempQ, 1)
    Answer.append(sum(Result))
    
print(Answer.index(min(Answer)) + 1)
