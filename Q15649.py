#New algorithm, help from https://jiwon-coding.tistory.com/21
N,M = map(int, input().split())
TheList = []

def Solve():
    if len(TheList) == M:
        print(' '.join(map(str, TheList)))
        return
    
    for i in range(1,N+1):
        if i not in TheList:
            TheList.append(i)
            Solve()
            TheList.pop()
Solve()
