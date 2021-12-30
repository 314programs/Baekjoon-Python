#More USACO practice
BouyListLen = int(input())
BouyList = [list(map(int, input().split())) for v in range(BouyListLen)]
Max = 0

for i in range(BouyListLen):
    Timing = [0]*1001
    print(BouyList[i])
    
    for j in range(BouyListLen):
        if i != j:
            for x in range (BouyList[j][0],BouyList[j][1]):
                Timing[x] = 1
            print(Timing)
    Max = max(Timing.count(1), Max)
print(Max)
