import heapq

NodeNum = int(input())
RoadNum = int(input())

RoadDict = {v:[] for v in range(1, NodeNum+1)}

#Organise the nodes and distances into a dictionary
for i in range(RoadNum):
    a,b,c = map(int, input().split())
    RoadDict[a].append([b,c])
    
Start, End = map(int, input().split())

#Dijkstra algorithm
def dijkstra(start, end, nodes):
    Distance = {v:float('inf') for v in range(1, nodes+1)}
    Distance[start] = 0 
    queue = [[Distance[start], start]]
    
    while queue:
        currentDistance, currentNode = heapq.heappop(queue)
        #If the current distance is bigger than the distance recorded, ignore. 
        if Distance[currentNode] < currentDistance:
            continue
            
        else:
            for newDestination, newDistance in RoadDict[currentNode]:
                theDistance = newDistance + currentDistance 
                #If the current distance is smaller than the distance recorded, change the distance of the new node
                if theDistance < Distance[newDestination]:
                    Distance[newDestination] = theDistance
                    #Push the node with the smallest distance
                    heapq.heappush(queue, [theDistance, newDestination])
            
    print(Distance[end])
    return 

dijkstra(Start, End, NodeNum)
