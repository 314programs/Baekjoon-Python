numList = list(map(int, input().split()))
numList.sort()
Result = ''
for item in numList:
    Result += str(item) + ' '
print(Result)
