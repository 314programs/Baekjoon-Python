#I love kruskal's algorithm
#I can even do these during mocks...
Computer_number = int(input())
Connection_number = int(input())
Connections = [list(map(int, input().split())) for v in range(Connection_number)]

Connections.sort(key = lambda x: x[2])
Parent = [v for v in range(Computer_number + 1)]
Max_Cost = 0

def find_parent(target):
    if Parent[target] == target:
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
        
for start, end, distance in Connections:
    if find_parent(start) != find_parent(end):
        Max_Cost += distance
        union(start, end)
        
print(Max_Cost)
