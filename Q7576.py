from collections import deque
import sys
input = sys.stdin.readline

width, height = map(int, input().split())
graphList = []
visited = []

#Take input and turn it into a graph using list
for i in range(height):
    graphList.append(list(map(int, input().split())))
    visited.append([0]*width)

Dx = [1,-1,0,0]
Dy = [0,0,1,-1]

WillVisit = deque([])
Count = 0
#Change the visited graph and make queue for visiting nodes
for h in range(height):
    for w in range(width):
        if graphList[h][w] == 1:
            WillVisit.append([h,w])
            visited[h][w] = 0
        elif graphList[h][w] == 0:
            visited[h][w] = -1
        else:
            visited[h][w] = -2
#While the queue is not empty, use BFS to calculate the next tomato growth
while WillVisit:
    temp = WillVisit.popleft()
    for i in range(4):
        Y = temp[0] + Dy[i]
        X = temp[1] + Dx[i]
        if Y < height and Y >= 0 and X < width and X >= 0 and visited[Y][X] == -1:
            WillVisit.append([Y,X])
            visited[Y][X] = visited[temp[0]][temp[1]] + 1
NoPrint = False
answer = 0 
#Calculate if there are non-grown tomatoes and also calculate max days taken
for h in range(height):
    for w in range(width):
        if visited[h][w] == -1:
            NoPrint = True
            break
        answer = max(answer, visited[h][w])
#Print
if not NoPrint:
    print(answer)
else:
    print('-1')
