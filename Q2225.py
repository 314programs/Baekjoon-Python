N, K = map(int, input().split())

dp = [[0 for v in range(N+1)] for v in range(K+1)]
dp[0][0] = 1

#How many numbers can be used
for k in range(1, K+1):
    #To form which number
    for n in range(N+1):
        #Subtract numbers till n to get maximum methods
        for l in range(n+1):
            #Find total number of methods that can be formed from k numbers to n
            dp[k][n] += dp[k-1][n-l]
            dp[k][n] %= 10**9
print(dp[K][N])
