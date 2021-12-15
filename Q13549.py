from collections import deque

Start, End = map(int, input().split())
Visited = [-1]*100001
Visited[Start] = 0
queue = deque([Start])

#BFS
while queue:
    Temp = queue.popleft()
    
    if Visited[End] != -1:
        print(Visited[End])
        break
#Teleporting does not have distacance, so append it at very left
    if Temp*2 <= 100000 and Visited[Temp*2] == -1:
        queue.appendleft(Temp*2)
        Visited[Temp*2] = Visited[Temp]
#Others just put into deque the normal way
    if Temp+1 <= 100000 and Visited[Temp+1] == -1:
        queue.append(Temp+1)
        Visited[Temp+1] = Visited[Temp]+1
    if Temp-1 >= 0 and Visited[Temp-1] == -1:
        queue.append(Temp-1)
        Visited[Temp-1] = Visited[Temp]+1

