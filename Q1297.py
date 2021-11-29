import math
Diagonal, Height, Width = map(int, input().split())
M = Diagonal/((Height**2 + Width**2)**0.5)
print(math.floor(M*Height), math.floor(M*Width))
