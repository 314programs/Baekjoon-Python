import sys
Height, Width = map(int, input().split())

AddedGraph = [[0]*(Width+1)]
for i in range(Height):
    theList = list(map(int, input().split()))
    Temp = [0]
    for i in range(Width):
        Temp.append(theList[i] + Temp[-1])
    AddedGraph.append(Temp)

TestCase = int(input())
Locations = []
for i in range(TestCase):
    Locations.append(list(map(int, input().split())))

    
for item in Locations:
    Result = 0
    for i in range(item[0], item[2]+1):
        Result += AddedGraph[i][item[3]] - AddedGraph[i][item[1]-1]
    print(Result)
