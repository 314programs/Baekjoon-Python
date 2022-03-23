Width = int(input())
Graph = list(map(int, input().split()))
DP = [-1 for v in range(Width+1)]
DP[1] = 0

#Minimum jumps for each column
for i in range(1, Width+1):
    #Jump from prev spaces
    for j in range(1, i+1):
        #If jump distance is enough
        if DP[j] != -1 and i-j <= Graph[j-1]:
            #If jump number is less or not filled
            if DP[i] == -1 or DP[i] > DP[j] + 1:
                DP[i] = DP[j] + 1
print(DP[Width])
