#Incredibly slow, improve later...
import copy
import sys
input = sys.stdin.readline

Height, Width = map(int, input().rstrip('\n').split())
Graph = [list(input()) for v in range(Height)]

#Down, up, right, left
Dx = [0,0,1,-1]
Dy = [1,-1,0,0]

Tries = -1

for h in range(Height):
    for w in range(Width):
        if Graph[h][w] == 'R':
            Red = [h, w]
        if Graph[h][w] == 'B':
            Blue = [h, w]
        if Graph[h][w] == 'O':
            Hole = [h, w]

def Moveball(Graph_temp, ball_type, other_type, Dir_X, Dir_Y):
    while True:
        TempY = ball_type[0] + Dir_Y
        TempX = ball_type[1] + Dir_X


        if Graph_temp[TempY][TempX] == '#':
            break
        
        elif Graph_temp[TempY][TempX] == 'O':
            ball_type = [TempY, TempX]
            break
        elif TempY == other_type[0] and TempX == other_type[1]:
            break
        elif Graph_temp[TempY][TempX] == '.':
            Graph_temp[TempY][TempX] = Graph_temp[ball_type[0]][ball_type[1]]
            Graph_temp[ball_type[0]][ball_type[1]] = '.'
            
        ball_type = [TempY, TempX]

    return ball_type


def backtrack(Graph_template, Dir_X, Dir_Y, prev_Dir, depth):
    global Directions
    if depth == 11: return
    
    for h in range(Height):
        for w in range(Width):
            if Graph_template[h][w] == 'R':
                Red = [h, w]
            if Graph_template[h][w] == 'B':
                Blue = [h, w]
            if Graph_template[h][w] == 'O':
                Hole = [h, w]

    global Tries

    Use_Graph = copy.deepcopy(Graph_template)
    Red_Before, Blue_Before = Red, Blue
    
    while True:
        Red = Moveball(Use_Graph, Red, Blue, Dir_X, Dir_Y)
        Blue = Moveball(Use_Graph, Blue, Red, Dir_X, Dir_Y)

        if Blue == Hole or Red == Hole:
            break

        if Red_Before == Red and Blue_Before == Blue:
            break

        Red_Before, Blue_Before = Red, Blue

    if Red == Hole and not Blue == Hole:
        if Tries == -1:
            Tries = depth
        else:
            Tries = min(depth, Tries)
        return
    if Blue == Hole:
        return

    for i in range(4):
        if i != prev_Dir:
            backtrack(Use_Graph, Dx[i], Dy[i], i, depth+1)

for i in range(4):
    backtrack(Graph, Dx[i], Dy[i], i, 1)
print(Tries)
