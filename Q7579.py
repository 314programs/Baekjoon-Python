#Knapsack
import sys
input = sys.stdin.readline

App_num, Max_memory = map(int, input().split())
Memory = list(map(int, input().split()))
Cost = list(map(int, input().split()))

Total_Cost = sum(Cost)

#I can just use 1 row to reduce memory and since using memory as a cost gets too big, use cost as memory since the max cost in question is 10000
DP = [0 for v in range(Total_Cost + 1)]
DP[0] = 0

#Knapsack algorithm but using 1 row
for x in range(1, App_num+1):
    for i in range(Total_Cost, Cost[x-1]-1, - 1):
        DP[i] = max(Memory[x-1] + DP[i-Cost[x-1]], DP[i])

#Calculate when it is over or equal to memory needed
for x in range(1, Total_Cost + 1):
    if DP[x] >= Max_memory:
        print(x)
        break
