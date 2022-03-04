#Topological sorting with other algorithms...
import sys
input = sys.stdin.readline

question_num, connection = map(int, input().split())
indegrees = [0 for v in range(question_num+1)]
outdegrees = [[] for v in range(question_num+1)]

queue = []

#Basic indegrees and outdegrees input
for i in range(connection):
    first, next = map(int, input().split())
    indegrees[next] += 1
    outdegrees[first].append(next)

for i in range(1, question_num+1):
    if indegrees[i] == 0:
        queue.append(i)

#Sort in reverse you cannot sort a deque each time meaning that popleft() will be impossible
queue.sort(reverse = True)

while queue:
    Temp = queue.pop()
    #Print each time
    print(Temp, end = " ")
    
    for item in outdegrees[Temp]:
        indegrees[item] -= 1
        if indegrees[item] == 0:
            queue.append(item)
            
    #Sort each time to update
    queue.sort(reverse = True)
        
