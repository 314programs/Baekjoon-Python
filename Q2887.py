import sys
input = sys.stdin.readline

#Input
planets = int(input())
planet_list = []
for i in range(planets):
    X_coord, Y_coord, Z_coord = map(int, input().split())
    planet_list.append([X_coord, Y_coord, Z_coord, i])

distance_list = []
parent = [v for v in range(planets+1)]
Total_distance = 0

#Closest in x, y, or z distance to minimise calculations
for i in range(3):
    planet_list.sort(key = lambda x: x[i])
    for x in range(planets-1):
        distance_list.append([planet_list[x][3],planet_list[x+1][3],abs(planet_list[x][i] - planet_list[x+1][i])])

distance_list.sort(key = lambda x: x[2])

#I love solving kruskal algorithms 
def find_parent(target):
    if parent[target] == target:
        return target
    parent[target] = find_parent(parent[target])
    return parent[target]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for start, end, distance in distance_list:
    if find_parent(start) != find_parent(end):
        Total_distance += distance
        union(start, end)
print(Total_distance)
