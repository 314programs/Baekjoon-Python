import copy
Dimension = int(input())
Graph = [list(map(int, input().split())) for v in range(Dimension)]
Max_num = 0

#Up, down, left, right
Dir_x = [0,0,1,-1]
Dir_y = [1,-1,0,0]

#Get maximum from the graph
def get_max(graph):
    temp_max = 0
    
    for y in range(Dimension):
        for x in range(Dimension):
            temp_max = max(temp_max, graph[y][x])
            
    return temp_max

#Move the numbers in the direction
def move(X_Dir, Y_Dir, copy_graph):
    while True:
        Move = 0
        X_Start, X_End = 0, Dimension
        Y_Start, Y_End = 0, Dimension
        
        #Set up movement
        if X_Dir == 1: X_Start = 1
        if X_Dir == -1: X_End = Dimension-1 
        if Y_Dir == 1: Y_Start = 1 
        if Y_Dir == -1: Y_End = Dimension-1 

        
        for y in range(Y_Start, Y_End):
            for x in range(X_Start, X_End):
                if copy_graph[y-Y_Dir][x-X_Dir] == 0 and copy_graph[y][x] != 0:
                    copy_graph[y-Y_Dir][x-X_Dir] = copy_graph[y][x]
                    copy_graph[y][x] = 0
                    Move += 1
        
        if Move == 0:
            return

#Function for total movement
def BFS(graph, X, Y):
    X_Dir = Dir_x[X]
    Y_Dir = Dir_y[Y]
    
    copy_graph = copy.deepcopy(graph)

    move(X_Dir, Y_Dir, copy_graph)
    
    X_Start, X_End = 0, Dimension
    Y_Start, Y_End = 0, Dimension
    X_Move, Y_Move = 1, 1

    #Set up for merging
    if X_Dir == 1: 
        X_Start = 1
        
    if X_Dir == -1: 
        X_End = Dimension-1 
        Temp_Start = X_Start
        X_Start = X_End-1
        X_End = Temp_Start-1
        X_Move = -1
        
    if Y_Dir == 1: 
        Y_Start = 1 
        
    if Y_Dir == -1: 
        Y_End = Dimension-1 
        Temp_Start = Y_Start
        Y_Start = Y_End-1
        Y_End = Temp_Start-1
        Y_Move= -1
    
    #Merge the number in the direction
    for y in range(Y_Start, Y_End, Y_Move):
        for x in range(X_Start, X_End, X_Move):
            if copy_graph[y-Y_Dir][x-X_Dir] == copy_graph[y][x] and copy_graph[y][x] != 0:
                copy_graph[y-Y_Dir][x-X_Dir] += copy_graph[y][x]
                copy_graph[y][x] = 0
                
    move(X_Dir, Y_Dir, copy_graph)
    return copy_graph
    

def Move_num(board, movement_num):
    global Max_num
    if movement_num == 5:
      #Get maximum value
        Max_num = max(Max_num, get_max(board))
        
    else:
      #Make graph in all directions using previous movement made
        for i in range(4):
            next_movement = BFS(board, i, i)
            Move_num(next_movement, movement_num + 1)

Move_num(Graph, 0)
print(Max_num)
