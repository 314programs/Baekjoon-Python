switches = int(input())
BallList = [0,1,0,0]

for i in range(switches):
    a,b = map(int, input().split())
    atemp = BallList[a]
    btemp = BallList[b]
    
    BallList[a] = btemp
    BallList[b] = atemp

for x in range(4):
    if BallList[x] == 1:
        print(x)
        break
