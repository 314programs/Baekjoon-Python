from collections import deque
import sys
input = sys.stdin.readline

Dimension = int(input())
Graph = []
GraphDict= {}
ResultGraph = []

#Make a list for results, dictionary for paths and append input into the graph
for i in range(Dimension):
    Graph.append(list(map(int, input().split())))
    ResultGraph.append(['0']*Dimension)
    GraphDict[i] = []

for y in range(Dimension):
    for x in range(Dimension):
        if Graph[y][x] == 1:
            GraphDict[y].append(x)
            
for i in range(Dimension):
    queue = deque([i])
#BFS for each number/row, use that information to change the result graph
    while queue:
        temp = queue.popleft()
        for item in GraphDict[temp]:
            if ResultGraph[i][item] == '0':
                ResultGraph[i][item] = '1'
                queue.append(item)
                
for item in ResultGraph:
    print(' '.join(item))
            
