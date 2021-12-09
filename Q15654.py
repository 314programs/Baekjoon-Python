#Very similar to the other N and M questions, backtracking but with different options
N,M = map(int, input().split())
NumList = list(map(int, input().split()))
NumList.sort()
PrintList = []
def Solve():
    if len(PrintList) == M:
        print(' '.join(map(str, PrintList)))
        return
    for i in range(N):
        if NumList[i] not in PrintList:
            PrintList.append(NumList[i])
            Solve()
            PrintList.pop()
Solve()
