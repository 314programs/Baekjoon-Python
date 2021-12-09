#Just add = to the if statement from Q15650
N,M = map(int, input().split())
PrintList = []
def Solve():
    if len(PrintList) == M:
        print(' '.join(map(str, PrintList)))
        return
    for i in range(1,N+1):
        if len(PrintList) == 0 or i >= PrintList[-1]:
            PrintList.append(i)
            Solve()
            PrintList.pop()
Solve()
