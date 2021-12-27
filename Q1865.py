import sys
input = sys.stdin.readline
TestCase = int(input())
for x in range(TestCase):
    NodeNum, RoadNum, PortalNum = map(int, input().split())
    Roads = [list(map(int, input().split())) for v in range(RoadNum)]
    Portals = [list(map(int, input().split())) for v in range(PortalNum)]
    Graph = []
    Possible = False

    #Make a graph
    for item in Roads:
        Graph.append([item[0], item[1], item[2]])
        Graph.append([item[1], item[0], item[2]])
        
    for item in Portals:
        Graph.append([item[0], item[1], -item[2]])
    
    #Bellman ford algorithm
    def Bellman(start, nodenum, n):
      #Start from all nodes
        distance = {v:0 for v in range(1, nodenum+1)}
        
        for i in range(nodenum):
            for j in range(n):
                currentNode = Graph[j][0]
                nextNode = Graph[j][1]
                cost = Graph[j][2]
                
                #Dijkstra
                if distance[currentNode] != float('inf') and distance[nextNode] > distance[currentNode] + cost:
                    distance[nextNode] = distance[currentNode] + cost
                    
                    #If the value has changed at the last moment it has a negative cycle
                    if i == nodenum-1:
                        return True
                    
        return False
        

    if Bellman(1, NodeNum, (RoadNum*2)+PortalNum):
        print('YES')
    else:
        print('NO')
