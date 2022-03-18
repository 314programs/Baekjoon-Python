#More DP practice
import sys
digit = int(sys.stdin.readline())
Divider = 10007
dp = [[0 for v in range(10)] for v in range(digit + 1)]
dp[1] = [1 for v in range(10)]

for i in range(2, digit + 1):
    for x in range(10):
        dp[i][x] = sum(dp[i-1][x:10])%Divider

print(sum(dp[digit]) % Divider)
