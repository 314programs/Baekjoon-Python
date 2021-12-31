import heapq

BusNum = int(input())
RoadNum = int(input())
RoadList = [[] for i in range(BusNum+1)]
#A backtracking list
Backtrack = list(range(BusNum + 1))

#Setting up graph
for x in range(RoadNum):
    a,b,c = map(int, input().split())
    RoadList[a].append([b, c])
    
start, end = map(int, input().split())

Distance = [float('inf') for v in range(BusNum+1)]

Backtrack[start] = 0
Distance[start] = 0
queue = [[0, start]]

#Dijkstra
while queue:
    CurrentDistance, CurrentNode = heapq.heappop(queue)
    if Distance[CurrentNode] < CurrentDistance:
        continue
    else:
        for NextNode, NextDistance in RoadList[CurrentNode]:
            Cost = NextDistance + CurrentDistance
            if Cost < Distance[NextNode]:
                Distance[NextNode] = Cost
                heapq.heappush(queue, [Cost, NextNode])
                Backtrack[NextNode] = CurrentNode

print(Distance[end])
result = [end]
#Backtrack to find out the city route
while Backtrack[end]:
    result.append(Backtrack[end])
    end = Backtrack[end]
    
print(len(result))
print(" ".join(map(str, reversed(result))))
                    
