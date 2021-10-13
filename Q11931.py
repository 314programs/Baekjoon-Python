import sys
input = sys.stdin.readline

CaseCount = int(input())
numList = []
for i in range(CaseCount):
    numList.append(int(input()))

numList.sort(reverse = True)
for item in numList:
    sys.stdout.write(str(item)+'\n')
