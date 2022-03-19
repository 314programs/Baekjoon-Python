#Practicing minimum spanning tree again
import sys
input = sys.stdin.readline

city_num, connection_num = map(int, input().split())
connections = [list(map(int, input().split())) for v in range(connection_num)]

connections.sort(key = lambda x: x[2])

Total_cost = 0
for s, e, distance in connections:
    Total_cost += distance

Short_cost = 0
Parent = [v for v in range(city_num + 1)]

def find_parent(target):
    if Parent[target] == target:
        return target
    Parent[target] = find_parent(Parent[target])
    return Parent[target]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        Parent[a] = b
    else:
        Parent[b] = a
        
#Kruskal
for start, end, distance in connections:
    if find_parent(start) != find_parent(end):
        union(start, end)
        Short_cost += distance

#Check if all cities are connected
def check():
    for i in range(1, city_num-1):
        if find_parent(i) != find_parent(i+1):
            print(-1)
            return
    print(Total_cost - Short_cost)
check()
