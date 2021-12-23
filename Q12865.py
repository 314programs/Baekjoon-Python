#I needed help since this is a new DP algorithm
#Help from source: https://gsmesie692.tistory.com/113
Item, MaxWeight = map(int, input().split())
Weight = []
Value = []

for i in range(Item):
    W, V = map(int, input().split())
    Weight.append(W)
    Value.append(V)

#2D graph
DP = [[0 for i in range(MaxWeight+1)]for v in range(Item + 1)]

for i in range(Item + 1):
    for w in range(MaxWeight+1):
        if i == 0 or w == 0:
            DP[i][w] = 0
            
        elif Weight[i-1] <= w:
            DP[i][w] = max(Value[i-1] + DP[i-1][w-Weight[i-1]], DP[i-1][w])
        
        else:
            DP[i][w] = DP[i-1][w]
print(DP[Item][MaxWeight])
