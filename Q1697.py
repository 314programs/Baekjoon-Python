from collections import deque
CurrentLocation, NeededLocation = map(int, input().split())
queue = [False]*1000001
Count = 0
if CurrentLocation == NeededLocation:
    print(0)
else:
    Tempqueue = deque([CurrentLocation])
    
    for item in Tempqueue:
        queue[item] = True
#BFS using a 1 dimensional list for each of the cases
    while True:
        Storage = deque([])
        if queue[NeededLocation] == True:
            break

        while Tempqueue:
            Temp = Tempqueue.popleft()
            if Temp*2 < 100001 and queue[Temp*2] == False:
                Storage.append(Temp*2)
                queue[Temp*2] = True
                
            if Temp+1 < 100001 and queue[Temp+1] == False:
                Storage.append(Temp+1)
                queue[Temp+1] = True
                
            if Temp-1 > -1 and queue[Temp-1] == False:
                Storage.append(Temp-1)
                queue[Temp-1] = True

        Count += 1
        Tempqueue = Storage


    print(Count)
