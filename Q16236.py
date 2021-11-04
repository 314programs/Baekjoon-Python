from collections import deque
import sys

input = sys.stdin.readline

Dimension = int(input())
Graph = []

for i in range(Dimension):
    Graph.append(list(map(int, input().split())))

#Set up graph, variables and direction
SharkSize = 2
FishCount = 0
SharkPosition = deque([[0,0]])
Time = 0

Dy = [0,0,1,-1]
Dx = [1,-1,0,0]

#BFS function to find nearest fish available
def BFS(queue):
    BreakOff = False
    MinDistance = 400
    PointList = []
    
    while queue:
        Temp = queue.popleft()

        for i in range(4):
            Y = Temp[0] + Dy[i]
            X = Temp[1] + Dx[i]
            if Y < Dimension and X < Dimension and Y > -1 and X > -1 and Visited[Y][X] > -3 and Visited[Y][X] < 0:
                Distance = Visited[Temp[0]][Temp[1]] + 1
                #Store the nearest fish in a list
                if Visited[Y][X] == -2 and Distance <= MinDistance:
                    BreakOff = True
                    if Distance < MinDistance:
                        PointList = []
                        MinDistance = Distance
                    PointList.append([Y,X])
                else:
                    queue.append([Y,X])
                Visited[Y][X] = Distance
                    
    if BreakOff and PointList:
      #Compare the stored fish to see which is at nearest to top left
        PointList.sort(key=lambda x:(x[0], x[1]))
        Graph[PointList[0][0]][PointList[0][1]] = 9
        return Visited[PointList[0][0]][PointList[0][1]]
    
    else:
        return 0      
    
#While loop to update the shark's size and available fish
while True:
    Count = 0
    Visited = [[0]*Dimension for v in range(Dimension)]
            
    for y in range(Dimension):
        for x in range(Dimension):
            #Cannot Pass
            if Graph[y][x] > SharkSize and Graph[y][x] < 7: 
                Visited[y][x] = -9
                
            #Fish
            elif Graph[y][x] < SharkSize and Graph[y][x] > 0:
                Visited[y][x] = -2
                
            #Shark
            elif Graph[y][x] == 9: 
                SharkPosition = deque([[y,x]])
                Graph[y][x] = 0
                
            #Pass
            elif Graph[y][x] == 0 or Graph[y][x] == SharkSize:
                Visited[y][x] = -1
    
    TempTime = BFS(SharkPosition)
        
    if TempTime != 0:
        Time += TempTime
        FishCount += 1
        
    else:
        print(Time)
        break
        
    if FishCount == SharkSize and SharkSize < 9:
        SharkSize += 1
        FishCount = 0
    
        

