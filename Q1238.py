import heapq

#Take input
StudentNum, RoadNum, Start = map(int, input().split())
Roads = [list(map(int, input().split())) for v in range(RoadNum)]
RoadGraph = [[] for v in range(StudentNum+1)]

for item in Roads:
    RoadGraph[item[0]].append([item[1], item[2]])

#Another Dijkstra algorithm, I needed more practices on Dijkstra
def Dijkstra(Start):
    Distance = [float('inf') for v in range(StudentNum+1)]
    Distance[Start] = 0
    queue = [[0, Start]]
    
    while queue:
        CurrentDistance, CurrentNode = heapq.heappop(queue)
        
        if Distance[CurrentNode] < CurrentDistance:
            continue
        
        else:
            for NextNode, NextDistance in RoadGraph[CurrentNode]:
                Cost = NextDistance + CurrentDistance
                if Cost < Distance[NextNode]:
                    Distance[NextNode] = Cost
                    heapq.heappush(queue, [Cost, NextNode])
                    
    return Distance

ResultList = [0]*(StudentNum+1)
#Calculate distance for returning to home from X
FromStart = Dijkstra(Start)

for i in range(1, StudentNum+1):
#Calculate distance for going to X from home
    DistanceList = Dijkstra(i)
    ResultList[i] = DistanceList[Start] + FromStart[i]

print(max(ResultList))

                
