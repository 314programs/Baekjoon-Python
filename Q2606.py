#Take input and make a connection of points
VertexNum = int(input())
ConnectionNum = int(input())
ConnectionList = []

for i in range(ConnectionNum):
    ConnectionList.append(list(map(int, input().split())))

GraphDict = {}
for x in range(101):
    GraphDict[x] = []
    
for item in ConnectionList:
    GraphDict[item[0]].append(item[1])
    GraphDict[item[1]].append(item[0])
        
#Use DFS to figure out the list of computers infected
visited = set()
DFSList = []
def dfs(visit, graph, node):
    if node not in visit:
        DFSList.append(str(node))
        visit.add(node)
        if node in graph:
            for nearby in graph[node]:
                dfs(visit, graph, nearby)

#Execute and print
dfs(visited, GraphDict, 1)
print(len(DFSList)-1)

