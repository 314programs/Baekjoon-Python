#This question killed me but I finally got it correct after few hours
import sys
input = sys.stdin.readline

dimension = int(input())
Graph = [list(map(int, input().split())) for v in range(dimension)]
max_count = 0

#Save coordnates based on which diagonal it is on
Visited_diagonal = [[] for v in range(dimension + dimension -1)]
Visited_diagonal_negative = [[] for v in range(dimension + dimension -1)]

Diagonal_visit = [0 for v in range(dimension + dimension -1)]
Diagonal_negative_visit = [0 for v in range(dimension + dimension -1)]

for y in range(dimension):
    for x in range(dimension):
        if Graph[y][x] == 1:
            Visited_diagonal[y+x].append([x-y+dimension-1, x, y])
            Visited_diagonal_negative[x-y+dimension-1].append([y+x, x, y])

CoordList = []

#Backtracking algorithm that uses index of Visited_diagonal
def Backtrack(diagonal_position):
    global max_count

    max_count = max(max_count, len(CoordList))
    Temp = True

    if diagonal_position >= dimension + dimension -2:
        return

    else:
        if len(Visited_diagonal[diagonal_position]) != 0:
            for item, x_coord, y_coord in Visited_diagonal[diagonal_position]:
              #Mark visits
                if Diagonal_visit[diagonal_position] == 0 and Diagonal_negative_visit[item] == 0:
                    Temp = False
                    CoordList.append([x_coord, y_coord])
                    Diagonal_visit[diagonal_position] = -1
                    Diagonal_negative_visit[item] = -1

                    Backtrack(diagonal_position + 1)

                    Diagonal_negative_visit[item] = 0
                    Diagonal_visit[diagonal_position] = 0

                    CoordList.pop()

        else:
            Backtrack(diagonal_position + 1)
        
        if Temp == True:
            Backtrack(diagonal_position + 1)

Backtrack(-1)

print(max_count)
