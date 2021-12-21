#Easy to code, hard to implement
import copy
Height, Width, Time = map(int, input().split())
Graph = []
for i in range(Height):
    Graph.append(list(map(int, input().split())))

Dy = [0,0,1,-1]
Dx = [1,-1,0,0]

AirCleaner = []

for t in range(Time):
    Dust = []
    #Spread
    for y in range(Height):
        for x in range(Width):
            if Graph[y][x] > 0:
                Dust.append([y,x, Graph[y][x]])
            if Graph[y][x] == -1:
                AirCleaner.append([y,x])
    
    for Temp in Dust:
        Spread = 0
        for i in range(4):
            Y = Temp[0] + Dy[i]
            X = Temp[1] + Dx[i]
            
            if -1<Y<Height and -1<X<Width and Graph[Y][X] >= 0:
                Spread += 1
                Graph[Y][X] += Temp[2]//5
                
        Graph[Temp[0]][Temp[1]] -= (Temp[2]//5)*Spread
        
    #Upper circulation
    for i in range(AirCleaner[0][0]-1,0,-1):
        Graph[i][0] = Graph[i-1][0]
    
    for i in range(0, Width-1):
        Graph[0][i] = Graph[0][i+1]
        
    for i in range(AirCleaner[0][0]):
        Graph[i][Width-1] = Graph[i+1][Width-1]
        
    for i in range(Width-1, 1, -1):
        Graph[AirCleaner[0][0]][i] = Graph[AirCleaner[0][0]][i-1]
    
    Graph[AirCleaner[0][0]][AirCleaner[0][1] + 1] = 0
    
    #Lower circulation
    for i in range(AirCleaner[1][0]+2, Height):
        Graph[i-1][0] = Graph[i][0]
    
    for i in range(Width-1):
        Graph[Height-1][i] = Graph[Height-1][i+1]
        
    for i in range(Height-1, AirCleaner[1][0]-1, -1):
        Graph[i][Width-1] = Graph[i-1][Width-1]
        
    for i in range(Width-1, 1, -1):
        Graph[AirCleaner[1][0]][i] = Graph[AirCleaner[1][0]][i-1]
        
    Graph[AirCleaner[1][0]][AirCleaner[1][1] + 1] = 0
    
    for item in Graph:
        print(' '.join(map(str, item)))
    print()

TotalDust = 0
for y in range(Height):
    for x in range(Width):
        if Graph[y][x] > 0:
            TotalDust += Graph[y][x]
            
print(TotalDust)
