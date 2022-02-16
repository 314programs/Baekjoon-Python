import sys
input = sys.stdin.readline

#Similar to other minimum spanning trees, but input of distance is in graph
Dimension = int(input())
Connection_Graph = [list(map(int, input().split())) for i in range(Dimension)]
Connections = []
Parent = [v for v in range(Dimension)]
Cost = 0

#Append connections through graph
for y in range(Dimension):
    for x in range(Dimension):
        #Changed y != x to y > x to avoid repetition, making this faster
        if y > x:
            Connections.append([y,x,Connection_Graph[y][x]])

#Basic kruskal algorithm
def Find_Parent(target):
    if Parent[target] == target:
        return target
    Parent[target] = Find_Parent(Parent[target])
    return Parent[target]

def Union(a, b):
    a = Find_Parent(a)
    b = Find_Parent(b)

    if a < b:
        Parent[b] = a
    else:
        Parent[a] = b

Connections.sort(key = lambda x: x[2])

for start, end, distance in Connections:
    if Find_Parent(start) != Find_Parent(end):
        Cost += distance
        Union(start, end)

#Print minimum cost
print(Cost)
