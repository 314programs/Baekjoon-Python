from collections import deque
import sys
input = sys.stdin.readline

#Take input and setup directions and visited graph
height, width = map(int, input().split())
MazeGraph = []
VisitedGraph = []

for i in range(height):
    Numbers = input()
    MazeGraph.append(list(Numbers))
    VisitedGraph.append([0]*width)

Dx = [1,-1,0,0]
Dy = [0,0,1,-1]

#Change visited graph accordingly to use it in BFS
for a in range(height):
    for b in range(width):
        if MazeGraph[a][b] == '1':
            VisitedGraph[a][b] = -1
        if MazeGraph[a][b] == '0':
            VisitedGraph[a][b] = -2
            
VisitedGraph[0][0] = 0
Q = deque([[0,0]])

#Run BFS and print
while Q:
    Temp = Q.popleft()
    
    for i in range(4):
        X = Temp[1] + Dx[i]
        Y = Temp[0] + Dy[i]
        if X < width and X > -1 and Y < height and Y > -1 and VisitedGraph[Y][X] == -1:
            Q.append([Y,X])
            VisitedGraph[Y][X] = VisitedGraph[Temp[0]][Temp[1]] + 1
    
print(VisitedGraph[height-1][width-1] + 1)
