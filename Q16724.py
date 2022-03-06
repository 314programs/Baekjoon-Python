#Long and inefficient code, will fix later...
import sys
input = sys.stdin.readline

Height, Width = map(int, input().split())
Graph = [list(input().strip()) for v in range(Height)]
Visited = [[0 for x in range(Width)] for y in range(Height)]
Count = 0

def BFS(Y,X,Dir, Mark):
    global New
    
    #For each directions
    if Dir == 'U':
        if Visited[Y-1][X] == 0:
            New = True
            Visited[Y-1][X] = Mark
            BFS(Y-1, X, Graph[Y-1][X], Mark)
        else:
            if Visited[Y-1][X] != Mark:
                New = False
            return
    
    if Dir == 'D':
        if Visited[Y+1][X] == 0:
            New = True
            Visited[Y+1][X] = Mark
            BFS(Y+1, X, Graph[Y+1][X], Mark)
        else:
            if Visited[Y+1][X] != Mark:
                New = False
            return
    
    if Dir == 'R':
        if Visited[Y][X+1] == 0:
            New = True
            Visited[Y][X+1] = Mark
            BFS(Y, X+1, Graph[Y][X+1], Mark)
        else:
            if Visited[Y][X+1] != Mark:
                New = False
            return

    if Dir == 'L':
        if Visited[Y][X-1] == 0:
            New = True
            Visited[Y][X-1] = Mark
            BFS(Y, X-1, Graph[Y][X-1], Mark)
        else:
            if Visited[Y][X-1] != Mark:
                #If cycle is not theirs
                New = False
            return

    
mark = 0

for y in range(Height): 
    for x in range(Width):
        New = False
        #Give them new mark to detect cycle
        mark += 1

        Visited[y][x] = mark
        BFS(y, x, Graph[y][x], mark)
        if New: 
            Count += 1

print(Count)
