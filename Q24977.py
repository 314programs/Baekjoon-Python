#Practicing USACO silver 
import sys
input = sys.stdin.readline

Connection_num = int(input())
Connections = []
Total = 0
for i in range(Connection_num):
    go, moos = map(int, input().split())
    Connections.append([i+1, go, moos])

Parents = [v for v in range(Connection_num+1)]

def Find_parent(target):
    if target == Parents[target]:
        return target
    Parents[target] = Find_parent(Parents[target])
    return Parents[target]

def Union(a, b):
    a = Find_parent(a)
    b = Find_parent(b)

    if a < b:
        Parents[b] = a
    else:
        Parents[a] = b

Connections.sort(key = lambda x: x[2], reverse = True)
for pos, go, distance in Connections:
    if Find_parent(pos) != Find_parent(go):
        Union(pos, go)
        Total += distance
print(Total)
