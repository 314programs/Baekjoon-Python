num = int(input())
dp = [0 for v in range(num + 1)]

for i in range(1, num + 1):
    #Since it is minimum, set a value higher then 0
    dp[i] = i
    #Compare value, current or subtracted with square
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i-j**2] + 1)
print(dp[num])
