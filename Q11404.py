#I cannot spell names (Sorry Warshall)
CityNum = int(input())
BusNum = int(input())
BusList = []

#Make a 2D list for the warshall algorithm
Yashal = [[float('inf') for i in range(CityNum)] for v in range(CityNum)]

#Input the given distances on the graph
for i in range(BusNum):
    Start, end, weight = map(int, input().split())
    Yashal[Start-1][end-1] =  min(weight, Yashal[Start-1][end-1])

#If start and end is the same, change it to 0 since no cost is needed    
for y in range(CityNum):
    for x in range(CityNum):
        if y == x:
            Yashal[y][x] = 0
    
#Node between start and end
for k in range(CityNum):
    #Start node
    for i in range(CityNum):
        #End node
        for j in range(CityNum):
            if Yashal[i][k] + Yashal[k][j] < Yashal[i][j]:
                Yashal[i][j] = Yashal[i][k] + Yashal[k][j]
                
for y in range(CityNum):
    for x in range(CityNum):
        if Yashal[y][x] == float('inf'):
            Yashal[y][x] = 0

for item in Yashal:
    print(' '.join(map(str, item)))
