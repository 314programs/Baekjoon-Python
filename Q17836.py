from collections import deque
import sys

Height, Width, Time = map(int, input().split())
Graph = []
Visited = []

for i in range(Height):
    Graph.append(list(map(int, input().split())))
    Visited.append([0]*Width)
    
SL = []

#Setting up visited graph
for h in range(Height):
    for w in range(Width):
        if Graph[h][w] == 0:
            Visited[h][w] = -1
        elif Graph[h][w] == 2:
            Visited[h][w] = -3
        else:
            Visited[h][w] = -2
            
queue = deque([[0,0]])
Visited[0][0] = 0

#BFS
def BFS():
    SwordFound = False
    Dy = [0,0,1,-1]
    Dx = [1,-1,0,0]
    
    while queue:
        Temp = queue.popleft()
        for i in range(4):
            Y = Temp[0] + Dy[i]
            X = Temp[1] + Dx[i]
            if Y < Height and Y > -1 and X < Width and X > -1 and (Visited[Y][X] == -1 or Visited[Y][X] == -3):
                queue.append([Y,X])
                Hour = Visited[Temp[0]][Temp[1]] + 1
                
                if Visited[Y][X] == -3:
                    SwordTime = Hour
                    SL.append(Y)
                    SL.append(X)
                    SwordFound = True
                    
                Visited[Y][X] = Hour
                
    if SwordFound:
        return SwordTime
    else:
        return -1
 
#ST = SwordTime
ST = BFS()

Reach = Visited[Height-1][Width-1]

#Set variables into high numbers if they are not possible in the condition given
if ST == -1:
    ST = 2**20
if Reach < 0:
    Reach = 2**20
if not SL:
    SL.append(-(2**20))
    SL.append(-(2**20))
    
#Calculate the distance to the the from the sword, since all walls can be broken
MinTime = min(Reach, (abs(Height-1-SL[0])) + (abs(Width-1-SL[1])) + ST)
    
if MinTime < Time:
    print(MinTime)
else:
    print('Fail')


