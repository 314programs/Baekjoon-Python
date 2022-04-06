#Was bored during freetime
import sys
from collections import deque
input = sys.stdin.readline

Height, Width = map(int, input().split())
Graph = [list(map(int, input().split())) for v in range(Height)]
Visited = [[0 for v in range(Width)] for v in range(Height)]
Island = 0

Dy = [0, 0, 1, -1, 1, 1, -1, -1]
Dx = [1, -1, 0, 0, 1, -1, 1, -1]

def BFS(Y, X):
    queue = deque([[Y, X]])

    while queue:
        Temp = queue.popleft()
        for i in range(8):
            Y_ = Temp[0] + Dy[i]
            X_ = Temp[1] + Dx[i]

            if 0 <= Y_ < Height and 0 <= X_ < Width and Graph[Y_][X_] > 0 and Visited[Y_][X_] == 0:
                Visited[Y_][X_] = -1
                queue.append([Y_, X_])


for H in range(Height):
    for W in range(Width):
        if Visited[H][W] == 0 and Graph[H][W] != 0:
            BFS(H,W)
            Island += 1
            
print(Island)
