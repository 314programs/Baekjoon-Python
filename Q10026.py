from collections import deque
import sys
input = sys.stdin.readline

Dimension = int(input())
Graph = []
Visited = []
Visited2 = []

for i in range(Dimension):
    Graph.append(list(input()))
    Visited.append([0]*Dimension)
    Visited2.append([0]*Dimension)

NormalColor = 0
AbnormalColor = 0

Dx = [1,-1,0,0]
Dy = [0,0,1,-1]

#Make BFS function since we need to use it twice
def BFS(a,b,v):
    Q = deque([[a,b]])
    v[a][b] = 1
    while Q:
        Temp = Q.popleft()

        for i in range(4):
            Y = Dy[i] + Temp[0]
            X = Dx[i] + Temp[1]
            if Y < Dimension and X < Dimension and X > -1 and Y > -1 and Graph[Temp[0]][Temp[1]] == Graph[Y][X] and v[Y][X] == 0:
                Q.append([Y,X])
                v[Y][X] = 1

#Run BFS for normal sight
for c in range(Dimension):
    for d in range(Dimension):
        if Visited[c][d] == 0:
            BFS(c,d, Visited)
            NormalColor += 1

#Change the graph to suit the abnormal sight
for a in range(Dimension):
    for b in range(Dimension):
        if Graph[a][b] == 'G':
            Graph[a][b] = 'R'
             
#Use BFS on the abnormal sight
for c in range(Dimension):
    for d in range(Dimension):
        if Visited2[c][d] == 0:
            BFS(c,d, Visited2)
            AbnormalColor += 1
#Print the results
print(NormalColor, AbnormalColor)
                

