import sys
input = sys.stdin.readline

wines = int(input())
wine_list = [int(input()) for v in range(wines)]

if wines <= 2:
    print(sum(wine_list))
else:
    dp = [[0, 0, 0] for v in range(wines + 1)]
    
    #1: First wine, 2: Second wine in a row
    dp[1] = [0, wine_list[0], 0]
    dp[2] = [0, wine_list[1], wine_list[1] + wine_list[0]]
  
    for i in range(3, wines + 1):
        #First possible wine selections, from 2 steps back choose the maximum selection between 1, 2
        dp[i][1] = max(dp[i-2][2], dp[i-2][1]) + wine_list[i-1]
        #Choose previous wine(1) + current wine or 2 steps back 2 wines in a row
        dp[i][2] = max(dp[i-1][1] + wine_list[i-1], dp[i-1][2])

    print(max(dp[wines]))
