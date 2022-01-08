import heapq
import sys

input = sys.stdin.readline

Nodes, Roads = map(int, input().split())
Graph = [[] for v in range(Nodes+1)]

for i in range(Roads):
    item = list(map(int, input().split()))
    Graph[item[0]].append([item[1], item[2]])
    Graph[item[1]].append([item[0], item[2]])
    
must1, must2 = map(int, input().split())

#Run a dijkstra algorithm
def dijkstra(start):
    Distance = [float('inf') for v in range(Nodes+1)]
    Distance[start] = 0
    queue = [[0, start]]
    
    while queue:
        CurrentCost, CurrentNode = heapq.heappop(queue)
        
        if Distance[CurrentNode] < CurrentCost:
            continue
        
        for NextNode, NextCost in Graph[CurrentNode]:
            Cost = NextCost + CurrentCost
            if Cost < Distance[NextNode]:
                Distance[NextNode] = Cost
                heapq.heappush(queue, [Cost, NextNode])
                
    return Distance

#Run the algorithm 3 times, from start, must1 and must2
From1 = dijkstra(1)
From_must1 = dijkstra(must1)
From_must2 = dijkstra(must2)

#Start -> must1 -> must2 -> End
One_to_Two = From1[must1] + From_must1[must2] + From_must2[Nodes]

#Start -> must2 -> must1 -> End
Two_to_One = From1[must2] + From_must2[must1] + From_must1[Nodes]

result = min(One_to_Two, Two_to_One)

#Check if distance is infinite
if result == float('inf'):
    print(-1)
else:
    print(result)
