ListLen = int(input())
ScoreList = []

for v in range(ListLen):
    ScoreList.append(int(input()))

ScoreList.sort()
Result = 0

for i in range(ListLen):
#This is |A-B|
    Result += abs(ScoreList[i] - (i+1))
    
print(Result)
    
