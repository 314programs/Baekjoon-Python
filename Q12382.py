#Dijkstra question to refresh my mind about dijkstra algorithms
import heapq, sys
input = sys.stdin.readline

Testcase = int(input())
for case in range(Testcase):
    Computer_num, Connection_num, Hacked_computer = map(int, input().split())
    Node_graph = [[] for v in range(Computer_num+1)]

    for i in range(Connection_num):
        a, b, time_take = map(int, input().split())
        Node_graph[b].append([a, time_take])
     
    #Dijkstra algorithm
    distance = [float('inf') for v in range(Computer_num+1)]
    distance[Hacked_computer] = 0
    queue = [[0, Hacked_computer]]

    while queue:
        current_time, current_destination = heapq.heappop(queue)

        if distance[current_destination] < current_time:
            continue

        for new_destination, new_time in Node_graph[current_destination]:
            cost = new_time + current_time
            if cost < distance[new_destination]:
                distance[new_destination] = cost
                heapq.heappush(queue, [cost, new_destination])
     
    #Get the last computer to be infected
    #I got confused on the definition of last computer at first...
    Temp = 0
    for item in distance:
        if item != float('inf'):
            Temp = max(item, Temp)

    print(len(distance) - distance.count(float('inf')), Temp)

