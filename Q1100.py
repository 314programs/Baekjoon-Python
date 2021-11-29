WModelList = ['W','B']*4
BModelList = ['B','W']*4
Count = 0
for i in range(8):
    TestList = list(map(str, input()))
    for a in range(8):
        if i == 0 or i%2 == 0:
            if WModelList[a] == 'W' and TestList[a] == 'F':
                Count += 1
        else:
            if BModelList[a] == 'W' and TestList[a] == 'F':
                Count += 1
print(Count)
