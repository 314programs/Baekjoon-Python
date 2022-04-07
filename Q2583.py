#Doing more graph revision
from collections import deque
import sys
input = sys.stdin.readline

Height, Width = map(int, input().split())
Graph = [list(map(int, input().split())) for v in range(Height)]
day = 0

Dy = [0,0,1,-1]
Dx = [1,-1,0,0]

def BFS(y,x):
    queue = deque([[y,x]])
    subtract_queue = []
    while queue:
        Temp = queue.popleft()
        Subtract = 0

        for i in range(4):
            Y_ = Temp[0] + Dy[i]
            X_ = Temp[1] + Dx[i]
            if 0 <= Y_ < Height and 0 <= X_ < Width and Visited[Y_][X_] == 0:
                if Graph[Y_][X_] > 0:
                    Visited[Y_][X_] = -1
                    queue.append([Y_, X_])
                else:
                    Subtract += 1

        subtract_queue.append([Temp[0],Temp[1],Subtract])
    
    for del_Y, del_X, subtraction in subtract_queue:
        Graph[del_Y][del_X] -= subtraction
        if Graph[del_Y][del_X] < 0:
            Graph[del_Y][del_X] = 0
    

while True:
    islands = 0
    Visited = [[0]*Width for v in range(Height)]
    for h in range(Height):
        for w in range(Width):
            if Graph[h][w] != 0 and Visited[h][w] == 0:
                Visited[h][w] = -1
                islands += 1
                BFS(h, w) 

    if islands == 0:
        print(0)
        break
    elif islands > 1:
        print(day)
        break

    day += 1
    
