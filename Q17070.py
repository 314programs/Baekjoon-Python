#Using BFS because I hate DP
import sys
input = sys.stdin.readline

Dimension = int(input())
Graph = [list(map(int, input().split())) for v in range(Dimension)]
count = 0

def BFS(Y,X,Direction):
    if Y == Dimension - 1 and X == Dimension - 1: 
        global count
        count += 1
    
    else:
        #Right
        if Direction == 0:
            if X+1 < Dimension:
                if Graph[Y][X+1] == 0: 
                    BFS(Y,X+1, 0)
                if Y+1 < Dimension and Graph[Y+1][X+1] == 0 and Graph[Y+1][X] == 0 and Graph[Y][X+1] == 0: 
                    BFS(Y+1, X+1, 1)
        
        #Diagonal
        elif Direction == 1:
            if X+1 < Dimension and Graph[Y][X+1] == 0: 
                BFS(Y,X+1, 0)
            if X+1 < Dimension and Y+1 < Dimension and Graph[Y+1][X+1] == 0 and Graph[Y+1][X] == 0 and Graph[Y][X+1] == 0: 
                BFS(Y+1, X+1, 1)
            if Y+1 < Dimension and Graph[Y+1][X] == 0: 
                BFS(Y+1,X, 2)
        
        #Down
        elif Direction == 2:
            if Y+1 < Dimension:
                if Graph[Y+1][X] == 0: 
                    BFS(Y+1,X, 2)
                if X+1 < Dimension and Graph[Y+1][X+1] == 0 and Graph[Y+1][X] == 0 and Graph[Y][X+1] == 0: 
                    BFS(Y+1, X+1, 1)
BFS(0,1,0)
print(str(count))
