import sys
input = sys.stdin.readline

#Should have named my variables nodes instead of connections but I decided to name them connections 
New_Connections_num, Exist_Connections_num = map(int, input().split())
New_Connections = [list(map(int, input().split())) for v in range(New_Connections_num)]
Exist_Connections = [list(map(int, input().split())) for v in range(Exist_Connections_num)]
New_Connections_Updated = []

#Parents list to update union connections
Parents = [v for v in range(New_Connections_num+1)]
Total_Distance = 0

#Farming experience using Kruskal at this point...
#Updating and finding parent
def Find_Parent(target):
    if Parents[target] == target:
        return target
    Parents[target] = Find_Parent(Parents[target])
    return Parents[target]

#Making union
def Union(a, b):
    a = Find_Parent(a)
    b = Find_Parent(b)

    if a < b:
        Parents[b] = a
    else:
        Parents[a] = b

#Unite exisiting connections
for start, end in Exist_Connections:
    Union(start-1, end-1)

#Making new connections using coordinates given
for i in range(New_Connections_num):
    for x in range(New_Connections_num):
        if i < x:
            New_Connections_Updated.append([i, x, ((New_Connections[i][0] - New_Connections[x][0])**2 + (New_Connections[i][1] - New_Connections[x][1])**2)**0.5])

#Sort list via distance for Kruskal
New_Connections_Updated.sort(key = lambda x: x[2])

for start, end, distance in New_Connections_Updated:
    if Find_Parent(start) != Find_Parent(end):
        Union(start, end)
        Total_Distance += distance

#Print formatted
print('{0:.2f}'.format(Total_Distance))
