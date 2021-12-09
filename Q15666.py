import sys
input = sys.stdin.readline
print = sys.stdout.write

N,M = map(int, input().split())
NumList = list(set(map(int, input().split())))
NumList.sort()

PrintList = []
ResultList = []


def Solve():
    if len(PrintList) == M:
        print(' '.join(map(str, PrintList))+'\n')
        return
    
    for i in range(len(NumList)):
        if len(PrintList) == 0 or NumList[i] >= PrintList[-1]:
            PrintList.append(NumList[i])
            Solve()
            PrintList.pop()

Solve()
