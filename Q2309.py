HeightList = []
for i in range(9):
    HeightList.append(int(input()))
    
for a in HeightList:
    for b in HeightList:
        if a != b and sum(HeightList)-a-b == 100:
            HeightList.pop(HeightList.index(a))
            HeightList.pop(HeightList.index(b))
HeightList.sort()

for item in HeightList:
    print(item)
