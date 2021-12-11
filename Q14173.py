#Practising more USACO formats
x1, y1, x2, y2 = map(int, input().split())
X1, Y1, X2, Y2 = map(int, input().split())

MinX1 = min(x1, X1)
MinY1 = min(y1, Y1)
MaxX2 = max(x2, X2)
MaxY2 = max(y2, Y2)

Multiply = max(MaxX2-MinX1, MaxY2 - MinY1)
print(Multiply**2)
