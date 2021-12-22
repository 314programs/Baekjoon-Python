#Very similar to quesiton 1967, except the change of input
#Copy and pasted the entire code
VertexNum = int(input())
NodeDict = {}

for i in range(1, VertexNum+1):
    NodeDict[i] = []
    
for i in range(VertexNum):
    VertexList = list(map(int, input().split()))
    for i in range(1, len(VertexList)-1,2):
        NodeDict[VertexList[0]].append([VertexList[i], VertexList[i+1]])

Visited = [0]*(VertexNum+1)

farweight = 0
farnode = 0

def DFS(node, weight):
    global farweight
    global farnode
    Visited[node] = 1
    for item in NodeDict[node]:
        if Visited[item[0]] == 0:
            currentweight = weight + item[1]
            if currentweight > farweight:
                farnode = item[0]
                farweight = currentweight
            DFS(item[0], weight + item[1])

DFS(1, 0)
temp = farnode
farweight = 0
farnode = 0
Visited = [0]*(VertexNum+1)

DFS(temp, 0)
print(farweight)
