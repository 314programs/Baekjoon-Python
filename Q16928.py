from collections import deque
import sys
input = sys.stdin.readline

#Set up lists
Ladder, Snake = map(int, input().split())
Dict = {}
for i in range(Ladder+Snake):
    a,b = map(int, input().split())
    Dict[a] = b
Visited = [0]*107

queue = deque([[1, 0]])
Visited[1] = 1
space = 1
Result = 10000

#Use BFS to get the minimum time
while queue:
    Vspace, count = queue.popleft()
    if Vspace >= 100:
        Result = min(Result, count)

    else:
#Loop for the dice numbers
        for i in range(1,7):
            space = i + Vspace
                
            if Visited[space] == 0:
                Visited[space] = 1
                if space in Dict:
                    queue.append([Dict[space], count+1])
                else:
                    queue.append([space, count + 1])

print(Result)
