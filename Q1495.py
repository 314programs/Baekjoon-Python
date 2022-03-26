#More DP
import sys
input = sys.stdin.readline

Volume_change_num, start_volume, max_volume = map(int, input().split())
Volume_change = list(map(int, input().split()))

DP = [[0]*(max_volume+1) for v in range(Volume_change_num+1)]
DP[0][start_volume] = 1

for i in range(Volume_change_num):
    for j in range(max_volume+1):
        if DP[i][j] == 1:
            if j + Volume_change[i] <= max_volume:
                DP[i+1][j + Volume_change[i]] = 1
            if j - Volume_change[i] >= 0:
                DP[i+1][j - Volume_change[i]] = 1

ans = -1
for i in range(max_volume+1):
    if DP[Volume_change_num][i] == 1:
        ans = max(i, ans)

print(ans)
