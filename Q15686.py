from itertools import combinations
Dimension, ChickenPlace = map(int, input().split())
Graph = []
for i in range(Dimension):
    Graph.append(list(map(int, input().split())))
Chickens = []
Houses = []

#Save locations for chicken and houses
for y in range(Dimension):
    for x in range(Dimension):
        if Graph[y][x] == 1:
            Houses.append([x,y])
        if Graph[y][x] == 2:
            Chickens.append([x,y])
#Use itertools to make all possible combination of chicken places
CombinationList = list(combinations(Chickens, ChickenPlace))
AnsList = []
#Calculate the minimum chicken distances needed
for item in CombinationList:
    Ans = 0
    for H in Houses:
        TempList = []
        for C in item:
            TempList.append(abs(C[1]-H[1]) + abs(C[0]-H[0]))
        Ans += min(TempList)
    AnsList.append(Ans)
print(min(AnsList))
