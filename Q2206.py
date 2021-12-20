from collections import deque

Height, Width = map(int, input().split())
Graph = []
Visited = []

for y in range(Height):
    Graph.append(list(map(int, input())))
    Visited.append([0]*Width)
    
Dy = [0,0,1,-1]
Dx = [1,-1,0,0]

#[0]: Wall or space, [1]: How much traveled, [2]: wall broken
for y in range(Height):
    for x in range(Width):
        if Graph[y][x] == 0:
            Visited[y][x] = [0, 0, 0]
        elif Graph[y][x] == 1:
            Visited[y][x] = [-1, 0, 0]
            
            
queue = deque([[0,0]])
Visited[0][0] = [-2, 0, 0]
#BFS
while queue:
    Temp = queue.popleft()
    for i in range(4):
        Y = Dy[i] + Temp[0]
        X = Dx[i] + Temp[1]
        
        #Append if it is in the graph and smaller or not visited than visited value
        if -1<Y<Height and -1<X<Width and Visited[Temp[0]][Temp[1]][2] < 2 and (Visited[Y][X][1] == 0 or Visited[Temp[0]][Temp[1]][1] + 1 < Visited[Y][X][1]):
            if Visited[Y][X][0] == 0:
                Visited[Y][X][1] = Visited[Temp[0]][Temp[1]][1] + 1
                Visited[Y][X][2] = Visited[Temp[0]][Temp[1]][2]
                
                #Append to left when no wall is broken, so that if it doesn't work it can try with broken wall
                if Visited[Temp[0]][Temp[1]][2] == 0:
                    queue.appendleft([Y,X])
                else:
                    queue.append([Y,X])
             
            elif Visited[Y][X][0] == -1:
                Visited[Y][X][1] = Visited[Temp[0]][Temp[1]][1] + 1
                Visited[Y][X][2] = Visited[Temp[0]][Temp[1]][2] + 1
                queue.append([Y,X])

#Print
Count = Visited[Height-1][Width-1][1]
if Count == 0 and Height != 1 and Width != 1:
    print(-1)
else:
    print(Count + 1)
    
