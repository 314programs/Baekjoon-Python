#I missed kruskal so I did one on python
import sys
input = sys.stdin.readline

uni_num, connection_num = map(int, input().split())
#-1 here!!!
unis = list(map(str, input().split()))
connections = []

for i in range(connection_num):
    s_, e_, d_ = map(int, input().split())
    if(unis[s_-1] != unis[e_ -1]):
        connections.append([s_, e_, d_])

Parent = [v for v in range(uni_num+1)]
connections.sort(key = lambda x: x[2])

def find_parent(target):
    if(Parent[target] == target):
        return target
    Parent[target] = find_parent(Parent[target])
    return Parent[target] 

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        Parent[b] = a
    else:
        Parent[a] = b

Total_distance = 0
roads = 0

for start, end, distance in connections:
    if find_parent(start) != find_parent(end) :
        union(start, end)
        Total_distance += distance
        roads += 1


if(roads == uni_num-1):
    print(Total_distance)
else:
    print(-1)


