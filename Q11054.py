#Using 11053's code and utilising it
ListLen = int(input())
NumList = list(map(int, input().split()))
Dp = [[0,0] for v in range(ListLen)]
Dp[0][0] = 1
Dp[-1][0] = 1

#Q11053.py
for i in range(1, ListLen):
    maximum = 0
    for x in range(i):
        if NumList[i] > NumList[x]:
            maximum = max(Dp[x][0], maximum)
            
    Dp[i][0] = maximum + 1

#Q11053.py but from the back
for i in range(ListLen-1, -1, -1):
    maximum = 0
    for x in range(ListLen-1, i-1, -1):
        if NumList[i] > NumList[x]:
            maximum = max(Dp[x][1], maximum)
            
    Dp[i][1] = maximum + 1
Max = 0
#Combine and subtract
for i in range(ListLen):
    Max = max(Max, Dp[i][0] + Dp[i][1])
print(Max-1)
