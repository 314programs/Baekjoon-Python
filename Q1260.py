VertexNum, ConnectionNum, StartNum = map(int, input().split())
ConnectionList = [list(map(int, input().split())) for v in range(ConnectionNum)]

#Make a list of points since points are both sided
GraphDict = {}
for x in range(1001):
    GraphDict[x] = []
    
for item in ConnectionList:
    GraphDict[item[0]].append(item[1])
    GraphDict[item[1]].append(item[0])
        

#DFS
visited = set()
DFSList = []
def dfs(visit, graph, node):
    if node not in visit:
        DFSList.append(str(node))
        visit.add(node)
        if node in graph:
            graph[node].sort()
            for nearby in graph[node]:
                dfs(visit, graph, nearby)
            
dfs(visited, GraphDict, StartNum)
print(' '.join(DFSList))

#BFS
BFS_visited = []
BFS_List = []
queue = []

def bfs(visit, graph, node):
    visit.append(node)
    queue.append(node)
    
    while queue:
        popped = queue.pop(0)
        BFS_List.append(str(popped))
        
        if popped in graph:
            graph[popped].sort()
            for nearby in graph[popped]:
                if nearby not in visit:
                    visit.append(nearby)
                    queue.append(nearby)

bfs(BFS_visited, GraphDict, StartNum)
print(' '.join(BFS_List))



