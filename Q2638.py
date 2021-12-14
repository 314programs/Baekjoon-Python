import copy
from collections import deque

#Basic input setup and imports
Height, Width = map(int, input().split())
CheeseGraph = []
VisitedTemplate = []
for h in range(Height):
    CheeseGraph.append(list(map(int, input().split())))
    VisitedTemplate.append([0]*Width)

Hour = -1
Count = 1
Dy = [0,0,1,-1]
Dx = [1,-1,0,0]

queue = deque([[0,0]])

while Count != 0:
    Count = 0
#Deepcopy is very useful in many situations since it makes individual modules
#I like making visited module with it when it is not timely limited
    Visit = copy.deepcopy(VisitedTemplate)
    queue = deque([[0,0]])
    Cheese = []
    
#Setup visited graph and change the melted cheese in the cheese graph
    for Y in range(Height):
        for X in range(Width):
            if CheeseGraph[Y][X] == 1:
                Visit[Y][X] = -1
                Cheese.append([Y,X])
                Count += 1
            if CheeseGraph[Y][X] == -1:
                CheeseGraph[Y][X] = 0
#BFS for the melted cheese
    while queue:
        Temp = queue.popleft()
        for i in range(4):
            Y = Temp[0] + Dy[i]
            X = Temp[1] + Dx[i]
            
            if -1<Y<Height and -1<X<Width and Visit[Y][X] == 0:
                Visit[Y][X] = 1
                queue.append([Y,X])
#Check if the cheese is melting          
    for Temp in Cheese:
        Air = 0
        for i in range(4):
            Y = Temp[0] + Dy[i]
            X = Temp[1] + Dx[i]
            if -1<Y<Height and -1<X<Width and Visit[Y][X] == 1:
                Air += 1
        if Air >= 2:
            CheeseGraph[Temp[0]][Temp[1]] = -1 
    Hour += 1
    
print(Hour)
