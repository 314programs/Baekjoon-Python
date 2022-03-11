#I needed to learn Bottleneck Travelling Salesman Problem
#Turns out easy ones involve backtracking...
import sys
input = sys.stdin.readline

City_num = int(input())
City_connection = [list(map(int, input().split())) for v in range(City_num)]
min_distance = float('inf')

for y in range(City_num):
    for x in range(City_num):
        if y != x and City_connection[y][x] == 0:
            City_connection[y][x] = float('inf')

Path_list = []
Visited = [0 for v in range(City_num)]

def find_distance(path):
    global min_distance
    Temp_distance = 0
    for i in range(City_num-1):
        Temp_distance += City_connection[path[i]][path[i+1]]
    Temp_distance += City_connection[path[-1]][path[0]]
    min_distance = min(Temp_distance, min_distance)

def backtrack():
    if len(Path_list) == City_num:
        find_distance(Path_list)
        return
    else:
        for i in range(City_num):
            if Visited[i] == 0:
                Path_list.append(i)
                Visited[i] = 1
                backtrack()
                Visited[i] = 0
                Path_list.pop()

backtrack()
print(min_distance)
