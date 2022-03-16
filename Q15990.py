#More DP
import sys
input = sys.stdin.readline

testcase = int(input())
Divider = 1000000009

DP = [[0,0,0,0] for v in range(100001)]

DP[1] = [0, 1, 0, 0]
DP[2] = [0, 0, 1, 0]
DP[3] = [0, 1, 1, 1]

for i in range(4, 100001):
    DP[i][1] = (DP[i-1][2] + DP[i-1][3])%Divider
    DP[i][2] = (DP[i-2][1] + DP[i-2][3])%Divider
    DP[i][3] = (DP[i-3][1] + DP[i-3][2])%Divider

for case in range(testcase):
    num = int(input())
    print(sum(DP[num])%Divider)
