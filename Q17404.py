#Very similar to Q1149 but ending color cannot be same as the starting color
#Took suggestion from aslanlee to increase the price of the starting houses except for the fixed one to kkeep one house fixed at a time
import sys
input = sys.stdin.readline

Rows = int(input())
Houses = [list(map(int, input().split())) for v in range(Rows)]
Costs = []

#Repeat 3 times for 3 fixed houses at the start
for x in range(3):
    DP = [[0,0,0] for v in range(Rows + 1)]
    #Set fixed house
    for k in range(3):
        if k != x:
            DP[1][k] = 1001
        else:
            DP[1][k] = Houses[0][k]
     
    #Copied algorithm from Q1149
    for i in range(2, Rows+1):
        DP[i][0] = Houses[i-1][0] + min(DP[i-1][1], DP[i-1][2])
        DP[i][1] = Houses[i-1][1] + min(DP[i-1][0], DP[i-1][2])
        DP[i][2] = Houses[i-1][2] + min(DP[i-1][0], DP[i-1][1])

    Temp = []
  
    #Calculate if it is not same as fixed house
    for k in range(3):
        if k != x:
            Temp.append(DP[-1][k])

    Costs.append(min(Temp))
print(min(Costs))
