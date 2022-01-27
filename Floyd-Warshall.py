Warshall = [[float('inf') for i in range(Dimension)] for v in range(Dimension)]

#Node between start and end
for k in range(Dimension):
    #Start node
    for i in range(Dimension):
        #End node
        for j in range(Dimension):
            if Warshall[i][k] + Warshall[k][j] < Warshall[i][j]:
                Warshall[i][j] = Warshall[i][k] + Warshall[k][j]
