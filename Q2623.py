#Doing topological sorting as a remind myself
from collections import deque
import sys
input = sys.stdin.readline

Singer_num, PD_num = map(int, input().split())
Indegrees = [0 for v in range(Singer_num+1)]
Outdegrees = [[] for v in range(Singer_num+1)]
Result = []

#Take in input, but since the first number is length, use [1:] to seperate them
for x in range(PD_num):
    Order = list(map(int, input().split()))
    Order = Order[1:]
    for i in range(1, len(Order)):
        Indegrees[Order[i]] += 1
    for i in range(len(Order)-1):
        Outdegrees[Order[i]].append(Order[i+1]) 

queue = deque([])

for i in range(1, Singer_num+1):
    if Indegrees[i] == 0: 
        Indegrees[i] = -1
        queue.append(i)

#Using BFS to do topological sorting
while queue:
    Temp = queue.popleft()
    Result.append(Temp)

    for item in Outdegrees[Temp]:
        Indegrees[item] -= 1
        if Indegrees[item] == 0:
            Indegrees[item] = -1
            queue.append(item)

#Print if it is possible
if len(Result) == Singer_num:
    for item in Result: print(item)
else:
    print(0)
