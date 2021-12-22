import sys
sys.setrecursionlimit(100000)
NodeCount = int(input())
#1 is an exception since it has no node connection
if NodeCount != 1:
    NodeDict = {}
    Visited = [0]*(NodeCount+1)

    for i in range(1,NodeCount+1):
        NodeDict[i] = []
#Make a dictionary for DFS, nodes connect in both directions
    for i in range(NodeCount-1):
        a,b,c = map(int, input().split())
        NodeDict[a].append([b,c])
        NodeDict[b].append([a,c])

    Visited = [0]*(NodeCount+1)

    farweight = 0
    farnode = 0
#DFS search
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
#DFS from the root to find the farthest node
    DFS(1, 0)
    temp = farnode
    farweight = 0
    farnode = 0
    Visited = [0]*(NodeCount+1)
#DFS from the farthest node
    DFS(temp, 0)
    print(farweight)
else: print(0)
    
