ListLen = int(input())
#Since he dies when his health becomes 0, make his MaxHealth 99 instead of 100
#I also will call health weight
MaxHealth = 99
HealthList = list(map(int, input().split()))
HappyList = list(map(int, input().split()))
#Make a DP List
DP = [[0 for i in range(MaxHealth+1)] for v in range(ListLen+1)]


for i in range(ListLen+1):
    for w in range(MaxHealth + 1):
        if i == 0 or w == 0:
            DP[i][w] = 0
        #Previous value or the current value + max value that can be made by subtracting the weight of current value
        elif HealthList[i-1] <= w:
            DP[i][w] = max(HappyList[i-1] + DP[i-1][w-HealthList[i-1]], DP[i-1][w])
        #Same as previous since the weight is bigger
        else:
            DP[i][w] = DP[i-1][w]
            
print(DP[-1][-1])
