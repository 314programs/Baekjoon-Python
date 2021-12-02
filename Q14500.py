import sys
input = sys.stdin.readline

Height, Width = map(int, input().split())
ShapeGraph = []

for i in range(Height):
    ShapeGraph.append(list(map(int, input().split())))

#Coordinate of shapes
#Did not enter this manually, made another code previously to detect a graph input and turn it into coordinates
Shapes = [[[0, 0, 0, 0], [0, 1, 2, 3]], [[0, 1, 2, 3], [0, 0, 0, 0]], [[0, 0, 1, 1], [0, 1, 0, 1]], [[0, 1, 2, 2], [0, 0, 0, 1]], [[0, 0, 0, 1], [0, 1, 2, 0]], [[0, 0, 1, 2], [0, 1, 1, 1]], [[0, 1, 1, 1], [2, 0, 1, 2]], [[0, 1, 2, 2], [1, 1, 0, 1]], [[0, 0, 0, 1], [0, 1, 2, 2]], [[0, 0, 1, 2], [0, 1, 0, 0]], [[0, 1, 1, 1], [0, 0, 1, 2]], [[0, 1, 1, 2], [0, 0, 1, 1]], [[0, 0, 1, 1], [1, 2, 0, 1]], [[0, 1, 1, 2], [1, 0, 1, 0]], [[0, 0, 1, 1], [0, 1, 1, 2]], [[0, 1, 1, 1], [1, 0, 1, 2]], [[0, 1, 1, 2], [0, 0, 1, 0]], [[0, 0, 0, 1], [0, 1, 2, 1]], [[0, 1, 1, 2], [1, 0, 1, 1]]]
maximum = 0

#Loop to check for every shape on graph
for h in range(Height):
    for w in range(Width):
        for item in Shapes:
            Temp = 0
            for i in range(4):
                if item[0][i]+h < Height and item[1][i]+w < Width:
                    Temp += ShapeGraph[item[0][i]+h][item[1][i]+w]
                else:
                    Temp = 0
                    break
                
            maximum = max(Temp, maximum)
        
print(maximum)
