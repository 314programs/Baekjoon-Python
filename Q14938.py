import heapq

NodeNum, SearchLim, PathNum = map(int, input().split())
NodeList = list(map(int, input().split()))
RoadList = [list(map(int, input().split())) for v in range(PathNum)]
Graph = {v:[] for v in range(1, NodeNum+1)}
Result = []

#Basic setup
for item in RoadList:
    Graph[item[0]].append([item[1], item[2]])
    Graph[item[1]].append([item[0], item[2]])

#Dijkstra function
def dijkstra(start):
    Distance = {v:float('inf') for v in range(1, NodeNum+1)}
    Distance[start] = 0
    queue = [[0, start]]
    
    while queue:
        CurrentDistance, CurrentDestination = heapq.heappop(queue)
        
        if Distance[CurrentDestination] < CurrentDistance:
            continue
        else:
            for NewDestination, NewDistance in Graph[CurrentDestination]:
                Cost = NewDistance + CurrentDistance
                if Cost < Distance[NewDestination]:
                    Distance[NewDestination] = Cost
                    heapq.heappush(queue, [Cost, NewDestination])
    
    return Distance
                    
for i in range(1, NodeNum+1):
#Dijkstra function for all nodes to find out the maximum
    Temp = dijkstra(i)
    Max = 0
    
    for v in range(1, NodeNum+1):
      #Compare the distance and add it to the value if it is within the search range
        if Temp[v] <= SearchLim:
            Max += NodeList[v-1]
    Result.append(Max)
    
print(max(Result))
