import sys
input = sys.stdin.readline
TestCase = int(input())

#Pythagoras function to calculate distance
def SquareRoot(x1, x2, y1, y2):
    X = x1 - x2
    Y = y1 - y2
    return (Y**2 + X**2)

for i in range(TestCase):
    Points = []
    for a in range(4):
        Points.append(list(map(int, input().split())))
    
    Points.sort(key = lambda x: (x[0], x[1]))
    Count = 0
    Length = SquareRoot(Points[0][0], Points[2][0], Points[0][1], Points[2][1])

#Checks distance between points
    if SquareRoot(Points[3][0], Points[1][0], Points[3][1], Points[1][1]) == Length: Count += 1
    if SquareRoot(Points[2][0], Points[3][0], Points[2][1], Points[3][1]) == Length: Count += 1
    if SquareRoot(Points[0][0], Points[1][0], Points[0][1], Points[1][1]) == Length: Count += 1
#To see if it is a square or a rhombus
    if SquareRoot(Points[3][0], Points[0][0], Points[3][1], Points[0][1]) == SquareRoot(Points[2][0], Points[1][0], Points[2][1], Points[1][1]): Count += 1
    
    if Count == 4: print(1)
    else: print(0)

    
