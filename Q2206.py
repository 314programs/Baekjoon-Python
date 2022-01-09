from collections import deque
import sys
input = sys.stdin.readline

Height, Width = map(int, input().split())
Graph = []
Visited = []

for i in range(Height):
    Graph.append(list(map(int, input().strip())))
    Visited.append([0]*Width)
    
#Basic direction
Dy = [0,0,1,-1]
Dx = [1,-1,0,0]

for h in range(Height):
    for w in range(Width):
        if Graph[h][w] == 0:
            #[0]: wall or empty space, [1]: distance travelled, [2]: wall broken
            Visited[h][w] = [0,0,False]
        else:
            Visited[h][w] = [-1,0,False]

Visited[0][0] = [0,0,False]

queue = deque([[0,0]])
wallqueue = deque([])
while queue or wallqueue:
    Temp = queue.popleft()
    
    for i in range(4):
        Y = Dy[i] + Temp[0]
        X = Dx[i] + Temp[1]
        
        #If not visited or have breaken wall to find a shorter path
        if -1<Y<Height and -1<X<Width and (Visited[Y][X][1] == 0 or (Visited[Temp[0]][Temp[1]][2] == True and Visited[Y][X][1] > Visited[Temp[0]][Temp[1]][1]+1)):
            #If space
            if Visited[Y][X][0] == 0:
                Visited[Y][X][1] = Visited[Temp[0]][Temp[1]][1] + 1
                if Visited[Temp[0]][Temp[1]][2] == True:
                    Visited[Y][X][2] = True
                    wallqueue.append([Y,X])
                else:
                    queue.append([Y,X])
            #If wall
            elif Visited[Y][X][0] == -1 and Visited[Temp[0]][Temp[1]][2] == False:
                Visited[Y][X][1] = Visited[Temp[0]][Temp[1]][1] + 1
                Visited[Y][X][2] = True
                wallqueue.append([Y,X])

    if len(queue) == 0:
        queue = wallqueue
        wallqueue = deque([])
    
result = Visited[Height-1][Width-1][1]

if result == 0:
    print(-1)
else:
    print(result+1)
