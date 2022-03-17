#Daily DP
pinary_length = int(input())
dp = [[0 for v in range(2)] for i in range(pinary_length+1)]

dp[1] = [0, 1]

for i in range(2, pinary_length + 1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[pinary_length]))
