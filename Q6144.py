#Surprised because there was less given memory
Charm, MaxWeight = map(int, input().split())

DP = [[0 for v in range(MaxWeight+1)] for x in range(2)]

#Since there must be less memory usage, only height of 2 can be used instead of charm+1
#It just needs 2 spaces, the previous and the current
#Control of 2 spaces can be done by using %
for c in range(1, Charm+1):
    Current_Weight, Current_Desire = map(int, input().split())
    for w in range(1, MaxWeight+1):
        if w < Current_Weight:
            DP[(c+1)%2][w] = DP[c%2][w]
        else:
            DP[(c+1)%2][w] = max(DP[c%2][w], Current_Desire + DP[c%2][w-Current_Weight])

print(DP[-1][-1])
