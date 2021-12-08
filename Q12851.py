from collections import deque
CurrentLocation, NeededLocation = map(int, input().split())
visit = [[-1,0]]*1000001
queue = deque([CurrentLocation])
StopLimit = 100000000

visit[CurrentLocation] = [0,0]
#Covering the exception
if CurrentLocation == NeededLocation:
    print(0)
    print(1)

else:
#Else Use BFS, but with an extra variable which measure the attempts
    while queue:
        Temp = queue.popleft()
        Add = 1 + visit[Temp][0]


        if visit[NeededLocation][0] != -1 and StopLimit == 100000000:
            StopLimit = Add

        if Temp*2 < 100001:
            if Add <= StopLimit and (visit[Temp*2][0] == Add or visit[Temp*2][0] <= 0): 
                queue.append(Temp*2)
                visit[Temp*2] = [Add, visit[Temp*2][1]+1]

        if Temp+1 < 100001:
            if Add <= StopLimit and (visit[Temp+1][0] == Add or visit[Temp+1][0] <= 0): 
                queue.append(Temp+1)
                visit[Temp+1] = [Add, visit[Temp+1][1]+1] 

        if Temp-1 > -1:
            if Add <= StopLimit and (visit[Temp-1][0] == Add or visit[Temp-1][0] <= 0): 
                queue.append(Temp-1)
                visit[Temp-1] = [Add, visit[Temp-1][1]+1]

    print(visit[NeededLocation][0])
    print(visit[NeededLocation][1])

        
