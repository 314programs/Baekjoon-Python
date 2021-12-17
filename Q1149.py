HouseNum = int(input())
PriceList = []
DPList = [[0,0,0]]

for i in range(HouseNum):
    PriceList.append(list(map(int, input().split())))
    DPList.append([0,0,0])

for i in range(3):
    DPList[1][i] = PriceList[0][i]

for i in range(2,HouseNum+1):
    DPList[i][0] = min(DPList[i-1][1], DPList[i-1][2]) + PriceList[i-1][0]
    DPList[i][1] = min(DPList[i-1][0], DPList[i-1][2]) + PriceList[i-1][1]
    DPList[i][2] = min(DPList[i-1][1], DPList[i-1][0]) + PriceList[i-1][2]
    
print(min(DPList[-1]))
