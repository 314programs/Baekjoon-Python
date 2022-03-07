import sys
input = sys.stdin.readline

Height, Width, Shark_num = map(int, input().split())
Graph = [[[] for x in range(Width)] for v in range(Height)]

for i in range(Shark_num):
    y, x, speed, direction, size = map(int, input().split())
    Graph[y-1][x-1].append([speed, direction, size])

Size_counter = 0

def move_shark(Y, X, speed, direction, size):
    Y_, X_ = Y, X
    Temp = [speed, direction, size]
    if direction == 1 or direction == 2:
        Speed_ = speed%((Height-1)*2)
    else:
        Speed_ = speed%((Width-1)*2)

    for i in range(Speed_):
        #Up
        if direction == 1:
            if Y_ - 1 >= 0:
                Y_ -= 1
            else:
                Y_ += 1
                direction = 2

        #Down
        elif direction == 2:
            if Y_ + 1 < Height:
                Y_ += 1
            else:
                direction = 1
                Y_ -= 1
            
        #Right
        elif direction == 3:
            if X_ + 1 < Width:
                X_ += 1
            else:
                direction = 4
                X_ -= 1

        #Left
        elif direction == 4:
            if X_ - 1 >= 0:
                X_ -= 1
            else:
                direction = 3
                X_ += 1
    Graph[Y_][X_].append([speed, direction, size])
    Graph[Y][X].pop(Graph[Y][X].index(Temp))


def detect_shark():
    #Detect and put into queue
    queue = []
    for y in range(Height):
        for x in range(Width):
            if Graph[y][x] != []:
                queue.append([y, x])
    
    for y, x in queue:
        move_shark(y,x, Graph[y][x][0][0], Graph[y][x][0][1], Graph[y][x][0][2])

    #Check if there are more then 1 shark in 1 square
    for y in range(Height):
        for x in range(Width):
            if len(Graph[y][x]) > 1:
                Graph[y][x].sort(key = lambda x: x[2], reverse = True)
                Graph[y][x] = [Graph[y][x][0]]

#Function for catching shark
def catch_shark(Column):
    for i in range(Height):
        if Graph[i][Column] != []:
            Temp = int(Graph[i][Column][0][2])
            Graph[i][Column] = []
            return Temp
    return 0

for i in range(Width):
    Size_counter += catch_shark(i)
    detect_shark()

    

print(Size_counter)
