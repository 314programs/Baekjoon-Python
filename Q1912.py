#Running out of ideas for writing comments on these DP practices
list_len = int(input())
num_list = list(map(int, input().split()))
dp = [0 for v in range(list_len + 1)]
dp[0] = -float('inf')
dp[1] = num_list[0]

for i in range(2, list_len+1):
    dp[i] = max(num_list[i-1], dp[i-1] + num_list[i-1])

print(max(dp))
