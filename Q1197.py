import sys
input = sys.stdin.readline
Nodes, Connections = map(int, input().split())
Input_List = [list(map(int, input().split())) for v in range(Connections)]
Total_distance = 0

Parents = [v for v in range(Nodes+1)]

#Sort based on distance
Input_List.sort(key = lambda x: x[2])

#Used Kruskal's algorithm
#Use union finid algorithm to make Kruskal's algorithm
def find_parent(target):
    if Parents[target] == target:
        return target
    Parents[target] = find_parent(Parents[target])
    return Parents[target]

#Making union of 2 nodes
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        Parents[b] = a
    else:
        Parents[a] = b
    

#If parent for nodes are different, make their parents the same and add up the distance
#Ignore if both parents are the same(in union)
for start_node, end_node, distance in Input_List:
    if find_parent(start_node) != find_parent(end_node):
        Total_distance += distance
        union(start_node, end_node)
    

print(Total_distance)
