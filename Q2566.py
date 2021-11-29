NumList = []
for i in range(9):
    NumList.append(list(map(int, input().split())))
Max = 0
Coord = [0,0]

for a in range(9):
    for b in range(9):
        if NumList[a][b] > Max:
            Max = NumList[a][b]
            Coord = [a, b]
print(Max)
print(Coord[0]+1, Coord[1]+1)
