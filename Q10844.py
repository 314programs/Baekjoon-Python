#4 high silvers... not a slight increase in level
num_length = int(input())
Divider = 10**9

DP = [[0 for v in range(10)] for i in range(num_length+1)]
DP[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, num_length+1):
    DP[i][0] = DP[i-1][1]%Divider
    DP[i][9] = DP[i-1][8]%Divider

    for v in range(1, 9):
        DP[i][v] = (DP[i-1][v-1] + DP[i-1][v+1]) % Divider

print(sum(DP[num_length]) % Divider)
