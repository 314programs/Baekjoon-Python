#Set up variables and input
import sys
input = sys.stdin.readline
VertexNum, ConnectionNum = map(int, input().split())
ConnectionList = []

#Get a dictionary of values
for h in range(ConnectionNum):
    ConnectionList.append(list(map(int, input().split())))
PointList = set()
GraphDict = {}
for x in range(1,VertexNum+1):
    GraphDict[x] = []
    
for item in ConnectionList:
    GraphDict[item[0]].append(item[1])
    GraphDict[item[1]].append(item[0])

#Use DFS algorithm to check if visited
Result = 0
visited = set()
def dfs(visit, graph, node):
        if node not in visit:
            visit.add(node)
            if node in graph:
                for nearby in graph[node]:
                    dfs(visit, graph, nearby)   

#Increase result if element was not visited
for t in range(1,VertexNum+1):
    if t not in visited:
        Result +=1
        dfs(visited, GraphDict, t)   

print(Result)
