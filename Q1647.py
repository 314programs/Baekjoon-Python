House_Num, Road_Num = map(int, input().split())
Roads = [list(map(int, input().split())) for v in range(Road_Num)]

Roads.sort(key = lambda x: x[2])
Parents = [v for v in range(House_Num + 1)]
Cost = 0

#Kruskal's algorithm
def Find_Parent(target):
    if Parents[target] == target:
        return target
    Parents[target] = Find_Parent(Parents[target])
    return Parents[target]

def Union(a, b):
    a = Find_Parent(a)
    b = Find_Parent(b)

    if a < b:
        Parents[b] = a
    else:
        Parents[a] = b

for start, end, distance in Roads:
    if Find_Parent(start) != Find_Parent(end):
      #Calculate final (most expensive) cost to subtract it later on since town can be divided into 2
        Final = distance
        Cost += distance
        Union(start, end)

#Subtract the most expensive cost since town can be divided by 2
print(Cost - Final)
