from collections import deque
import sys
input = sys.stdin.readline

Dimension = int(input())
GraphList = []

#Take input and turn it into a graph
for i in range(Dimension):
    GraphList.append(list(input()))

#Use BFS to calculate how many houses are grouped together
def BFS(y,x):
    HouseCount = 0
    Dx = [1,-1,0,0]
    Dy = [0,0,1,-1]
    queue = deque([[y,x]])
    GraphList[y][x] = '-1'
    
    while queue:
        Temp = queue.popleft()
        HouseCount += 1
        
        for i in range(4):
            X = Dx[i] + Temp[1]
            Y = Dy[i] + Temp[0]
            
            if X < Dimension and X > -1 and Y < Dimension and Y > -1 and GraphList[Y][X] == '1':
                queue.append([Y,X])
                GraphList[Y][X] = '-1'
    return HouseCount

Count = []

#Run a loop to call functions each time there is a house
for a in range(Dimension):
    for b in range(Dimension):
        if GraphList[a][b] == '1':
            Count.append(BFS(a,b))

Count.sort()

print(len(Count))
for item in Count:
    print(item)
