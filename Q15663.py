#May try to imrpove later using BFS
import sys
input = sys.stdin.readline
print = sys.stdout.write
N,M = map(int, input().split())
NumList = list(map(int, input().split()))
NumList.sort()
PrintList = []
Result = []


def Solve():
    if len(PrintList) == M:
        Ans = ''
        for item in PrintList:
            Ans += str(NumList[item]) + ' '
            
        if Ans not in Result:
            Result.append(Ans)
            print(Ans + '\n')
        return
    
    for i in range(N):
        if len(PrintList) == 0 or i not in PrintList:
            PrintList.append(i)
            Solve()
            PrintList.pop()

Solve()
