#Practice even more DP
num_list_len = int(input())
num_list = list(map(int, input().split()))
dp = [0 for v in range(num_list_len+1)]

for i in range(1, num_list_len+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j]+num_list[j-1])

print(dp[-1])
