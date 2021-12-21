#Just use 11053's file but change line 10's > to <
ListLen = int(input())
NumList = list(map(int, input().split()))
Dp = [0]*ListLen
Dp[0] = 1

for i in range(1, ListLen):
    maximum = 0
    for x in range(i):
        if NumList[i] < NumList[x]:
            maximum = max(Dp[x], maximum)
            
    Dp[i] = maximum + 1
print(max(Dp))
