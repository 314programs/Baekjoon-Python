from collections import deque
import sys
input = sys.stdin.readline

#Take input and set up graphs
width, height, layer = map(int, input().split())
graphList = []
visited = []

for a in range(layer):
    Temp = []
    Temp2 = []
    for b in range(height):
        Temp.append(list(map(int, input().split())))
        Temp2.append([0]*width)
    graphList.append(Temp)
    visited.append(Temp2)

Queue = deque([])

Dx = [1,-1,0,0,0,0]
Dy = [0,0,1,-1,0,0]
Dz = [0,0,0,0,1,-1]


for a in range(layer):
    for b in range(height):
        for c in range(width):
            if graphList[a][b][c] == 0:
                visited[a][b][c] = -1
            elif graphList[a][b][c] == 1:
                Queue.append([a,b,c])
                visited[a][b][c] = 0

#Use BFS similar to 7576 except adding the Z axis
while Queue:
    Temp = Queue.popleft()
    for i in range(6):
        Z = Temp[0] + Dz[i]
        Y = Temp[1] + Dy[i]
        X = Temp[2] + Dx[i]
        if Z > -1 and Z < layer and Y > -1 and Y < height and X > -1 and X < width and visited[Z][Y][X] == -1:
            visited[Z][Y][X] = visited[Temp[0]][Temp[1]][Temp[2]] + 1
            Queue.append([Z,Y,X])

#Check for the maximum and count of unripe tomatoes
Answer = 0
Print = True
for a in range(layer):
    for b in range(height):
        for c in range(width):
            if visited[a][b][c] == -1:
                Print = False
            Answer = max(visited[a][b][c], Answer)
#Print       
if Print:
    print(Answer)
else:
    print('-1')

