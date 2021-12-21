#I tried backtracking, but since the list can be long as 1000, DP must be used
ListLen = int(input())
NumList = list(map(int, input().split()))
#Set DP List
Dp = [0]*ListLen
Dp[0] = 1

#Loop from 1 to the end of the list, since 1 is already set
for i in range(1, ListLen):
    maximum = 0
#Find the number before the current index i that is smaller, add it to the maximum
    for x in range(i):
        if NumList[i] > NumList[x]:
            maximum = max(Dp[x], maximum)
            
    Dp[i] = maximum + 1
print(max(Dp))
