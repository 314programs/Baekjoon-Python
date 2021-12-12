#Needed deepcopy since the graph copied kept changing its value
from itertools import combinations
from collections import deque
import copy

Height, Width = map(int, input().split())
Graph = []
for i in range(Height):
    Graph.append(list(map(int, input().split())))

#Basic setup and directions
PossiblePlacements = []
TempList = []
PossibleCombinations = []
Savedqueue = []
MinSpread = 0

Dx = [0,0,1,-1]
Dy = [1,-1,0,0]

for y in range(Height):
    for x in range(Width):
        if Graph[y][x] == 0:
            PossiblePlacements.append([y,x])
        if Graph[y][x] == 2:
            Savedqueue.append([y,x])

#Itertools my beloved
Comb = list(combinations(PossiblePlacements,3))

for i in range(len(Comb)):
    queue = deque([v for v in Savedqueue])
    TempGraph = copy.deepcopy(Graph)
    
    for x in range(3):
        TempGraph[Comb[i][x][0]][Comb[i][x][1]] = 1
#BFS
    while queue:
        Temp = queue.popleft()
        for i in range(4):
            Y = Temp[0] + Dy[i]
            X = Temp[1] + Dx[i]
            if Y > -1 and X > -1 and X < Width and Y < Height and TempGraph[Y][X] == 0:
                queue.append([Y,X])
                TempGraph[Y][X] = 2
                
                
    TotalCount = 0
    for item in TempGraph:
        TotalCount += item.count(0)
    
    if TotalCount > MinSpread:
        MinSpread = TotalCount
        
print(MinSpread)
