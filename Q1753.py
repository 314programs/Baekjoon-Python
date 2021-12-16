import heapq, sys
input = sys.stdin.readline

#Make a dictionary for graph
NodeNum, Line = map(int, input().split())
StartNode = int(input())
NodeGraph = {v: [] for v in range(1, NodeNum+1)}
for i in range(Line):
    Start, End, Dist = map(int, input().split())
    NodeGraph[Start].append([End, Dist])

#Use dijkstra algorithm, I will call it dj for short
def dj(start):
  
#Make the distance infinate so that it can be compared later
    distances = {v: float('inf') for v in range(1, NodeNum+1)}
    distances[start] = 0
    queue = [[distances[start], start]]
    
    while queue:
        currentDistance, currentDestination = heapq.heappop(queue)
#No need to compare when the current distance is bigger
        if distances[currentDestination] < currentDistance:
            continue
            
        for newDestination, newDistance in NodeGraph[currentDestination]:
            distance = currentDistance + newDistance
#If new distance is smaller than the saved distance, save the new distance as the old one
            if distance < distances[newDestination]:
                distances[newDestination] = distance
                heapq.heappush(queue,[distance, newDestination])
    return distances
            
    
distances = dj(StartNode)

#Print one by one
for i in range(1,NodeNum+1):
    if distances[i] == float('inf'):
        print('INF')
    else:
        print(distances[i])
