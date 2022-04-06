#BFS practice..?
from collections import deque
import sys
input = sys.stdin.readline

Destination_X, Destination_Y, Puddle_num = map(int, input().split())
Destination_X += 500
Destination_Y += 500

Visited = [[0 for k in range(1001)] for v in range(1001)]
for i in range(Puddle_num):
    X_, Y_ = map(int, input().split())
    Visited[Y_+500][X_+500] = -1

queue = deque([[500, 500]])

Dy = [0,0,1,-1]
Dx = [1,-1,0,0]

while queue:
    Temp = queue.popleft()

    for i in range(4):
        X = Temp[1] + Dx[i]
        Y = Temp[0] + Dy[i]

        if 0 <= X <= 1000 and 0 <= Y <= 1000 and Visited[Y][X] == 0:
            Visited[Y][X] = Visited[Temp[0]][Temp[1]] + 1
            queue.append([Y, X])
    
    if Visited[Destination_Y][Destination_X] != 0:
        print(Visited[Destination_Y][Destination_X])
        break
