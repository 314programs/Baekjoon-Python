import sys
input = sys.stdin.readline

interview = int(input())
time = []
profit = []
dp = [0 for v in range(interview+1)]

for i in range(interview):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

for i in range(interview):
    if i + time[i] <= interview:
        dp[i + time[i]] = max(dp[i + time[i]], dp[i] + profit[i])
    dp[i + 1] = max(dp[i+1], dp[i])

print(dp[interview])
