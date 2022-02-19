#Trying topological sort algorithm
#Uses BFS type of algorithm
from collections import deque
import sys
input = sys.stdin.readline

Students, Comparisons = map(int, input().split())
CompareList = [list(map(int, input().split())) for v in range(Comparisons)]
Indegrees = [0 for v in range(Students+1)]
Outdegrees = [[] for v in range(Students+1)]
Val_Zero = deque([])

#Measure how many indegrees and outdegrees there are
for start, end in CompareList:
    Indegrees[end] += 1
    Outdegrees[start].append(end)

for i in range(1, Students+1):
    if Indegrees[i] == 0:
        #Mark as visited
        Indegrees[i] = -1
        Val_Zero.append(i)


while Val_Zero:
    Temp = Val_Zero.popleft()

    for item in Outdegrees[Temp]:
        Indegrees[item] -= 1
    
    for i in range(1, Students+1):
        if Indegrees[i] == 0:
            Indegrees[i] = -1
            Val_Zero.append(i)

    print(Temp, end = ' ')
