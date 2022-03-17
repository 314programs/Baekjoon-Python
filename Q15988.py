import sys
input = sys.stdin.readline

testcase = int(input())
Divider = 1000000009

dp = [0 for v in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%Divider
        

for case in range(testcase):
    num = int(input())
    print(dp[num]%Divider)
