Dy = [0,0,1,-1,1,1,-1,-1]
Dx = [1,-1,0,0,1,-1,1,-1]
while True:
    height, width = map(int, input().split())
    Graph = []
    if height == 0 and width == 0:
        break
    for i in range(height):
        Graph.append(list(map(str, input())))
    
    for h in range(height):
        for w in range(width):
            if Graph[h][w] == '.':
                Graph[h][w] = 0
                for i in range(8):
                    Y = Dy[i] + h
                    X = Dx[i] + w
                    if Y < height and Y > -1 and X < width and X > -1 and Graph[Y][X] == '*':
                        Graph[h][w] += 1
                Graph[h][w] = str(Graph[h][w])
    for item in Graph:
        print(''.join(item))

