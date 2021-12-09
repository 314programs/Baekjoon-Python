#Same logic, different if code from other N and M questions
N,M = map(int, input().split())
NumList = list(map(int, input().split()))
NumList.sort()
PrintList = []
def Solve():
    if len(PrintList) == M:
        print(' '.join(map(str, PrintList)))
        return
    
    for i in range(N):
        if len(PrintList) == 0 or PrintList[-1] <= NumList[i]:
            PrintList.append(NumList[i])
            Solve()
            PrintList.pop()
Solve()
