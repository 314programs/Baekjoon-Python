#Copy and paste code from Q2239
#Just change input and output slightly
import sys
input = sys.stdin.readline
Sudoku = []
Empty = []

for i in range(9):
    Sudoku.append(list(map(int, input().split())))

for y in range(9):
    for x in range(9):
        if Sudoku[y][x] == 0:
            Empty.append([y,x])

def Row_Check(index, val):
    y = Empty[index][0]
    if val not in Sudoku[y]:
        return True
    
    return False
    
def Column_Check(index, val):
    x = Empty[index][1]
    
    for i in range(9):
        if Sudoku[i][x] == val:
            return False
    
    return True
    
def Square_Check(index, val):
    y = Empty[index][0]
    x = Empty[index][1]
    
    for y_ in range(y//3 * 3, ((y//3 + 1)*3)):
        for x_ in range(x//3 * 3, ((x//3 + 1)*3)):
            if Sudoku[y_][x_] == val:
                return False
            
    return True

def Backtrack(index): 
    if index == len(Empty):
        return
    
    for i in range(1,10):
        if Row_Check(index, i) and Column_Check(index, i) and Square_Check(index, i) and Sudoku[Empty[index][0]][Empty[index][1]] == 0:
            Sudoku[Empty[index][0]][Empty[index][1]] = i
            Backtrack(index+1)
    
    if Sudoku[Empty[index][0]][Empty[index][1]] == 0:
        Sudoku[Empty[index-1][0]][Empty[index-1][1]] = 0
        return
    
    
Backtrack(0)

for item in Sudoku:
    print(' '.join(map(str, item)))
