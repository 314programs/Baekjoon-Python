Star_Num = int(input())
#Take input of coordinates
Star_List = [list(map(float, input().split())) for v in range(Star_Num)]
Parent = [v for v in range(Star_Num+1)]
Cost = 0

#Use coordinates as nodes by numbering them by i
Star_Connections = []

#Use pythagoras theorem to calculate the distance between start and end
for x in range(Star_Num):
    for y in range(Star_Num):
        if x < y:
            Star_Connections.append([x, y, ((Star_List[x][0] -  Star_List[y][0])**2 + (Star_List[x][1] -  Star_List[y][1])**2)**0.5])

Star_Connections.sort(key = lambda x: x[2])

#Use the kruskal algorithm
def find_parent(target):
    if Parent[target] == target:
        return target
    Parent[target] = find_parent(Parent[target])
    return Parent[target]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        Parent[b] = a
    else:
        Parent[a] = b

for start, end, distance in Star_Connections:
    if find_parent(start) != find_parent(end):
        Cost += distance
        union(start, end)

#Print as 2 decimal place float
print("{0:.2f}".format(Cost))
