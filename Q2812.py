import sys
input = sys.stdin.readline

Length, DeleteNum = map(int, input().split())
Needed = Length - DeleteNum

Number = int(input())
numList = [int(v) for v in str(Number)]
ResultList = []

for i in range(Length):
  
#Delete when the end of the result if smaller than the current number
    while DeleteNum > 0 and ResultList:
        if ResultList[-1] < numList[i]:
            ResultList.pop()
            DeleteNum -= 1
            
        else:
            break
            
    ResultList.append(numList[i])

#Print
for i in range(Needed):
    print(ResultList[i], end='')
            
