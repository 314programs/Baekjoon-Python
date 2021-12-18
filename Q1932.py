TriangleHeight = int(input())
Triangle = [list(map(int, input().split())) for x in range(TriangleHeight)]
Dp = [[0]*(x+1) for x in range(TriangleHeight)]

#Case exception
if TriangleHeight == 1:
    print(Triangle[0][0])

elif TriangleHeight > 1:
#Basic setup
    Dp[0][0] = Triangle[0][0]
    Dp[1][0] = Triangle[1][0] + Dp[0][0]
    Dp[1][1] = Triangle[1][1] + Dp[0][0]

    for i in range(2, TriangleHeight):
#For the first and the last node
        Dp[i][0] = Triangle[i][0]+Dp[i-1][0]
        Dp[i][1] = max(Triangle[i][1]+Dp[i-1][0], Dp[i][1])
        Dp[i][len(Triangle[i])-1] = Triangle[i][len(Triangle[i])-1] + Dp[i-1][-1]
        Dp[i][len(Triangle[i])-2] = max(Triangle[i][len(Triangle[i])-2] + Dp[i-1][-1], Dp[i][len(Triangle[i])-2])
#For the other nodes in between, right or left
        for x in range(1,len(Triangle[i-1])-1):
            Dp[i][x] = max(Dp[i][x], Triangle[i][x] + Dp[i-1][x])
            Dp[i][x+1] = max(Dp[i][x+1], Triangle[i][x+1] + Dp[i-1][x])

    print(str(max(Dp[-1])))
        
