BingoCard = []
for i in range(5):
    BingoCard.append(list(map(int, input().split())))
CalledList = []
for i in range(5):
    Temp = list(map(int, input().split()))
    for item in Temp:
        CalledList.append(item)

print(CalledList)
Count = 0
Bingo = 0

for item in CalledList:
    Bingo = 0
    for h in range(5):
        for i in range(5):
            if BingoCard[h][i] == item:
                BingoCard[h][i] = 0

    for item in BingoCard:
        if item.count(0) == 5:
            Bingo += 1

    for a in range(5):
        Total = 0
        for b in range(5):
            Total += BingoCard[b][a]

        if Total == 0:
            Bingo += 1

    if BingoCard[0][0] + BingoCard[1][1] + BingoCard[2][2] + BingoCard[3][3] + BingoCard[4][4] == 0:
        Bingo += 1
    if BingoCard[0][4] + BingoCard[1][3] + BingoCard[2][2] + BingoCard[3][1] + BingoCard[4][0] == 0:
        Bingo += 1
    Count += 1

    if Bingo >= 3:
        break
        
print(Count)
                
        
