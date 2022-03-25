#Similar to 11066
#Should find faster solution using for loop
import sys
input = sys.stdin.readline

cases = int(input())
multiplication = [list(map(int, input().split())) for v in range(cases)]
dp = [[-1]*(cases) for v in range(cases)]


def find_min(start, end):
    if start == end:
        return 0
    if end - start == 1:
        dp[start][end] = multiplication[start][0] * multiplication[start][1] * multiplication[end][1]
        return dp[start][end]
    if dp[start][end] != -1:
        return dp[start][end]

    ans = dp[start][end]
    
    for i in range(start, end):
        temp = find_min(start, i) + find_min(i+1, end)
        if ans == -1 or ans > temp + multiplication[start][0] * multiplication[i][1] * multiplication[end][1]:
            ans = temp + multiplication[start][0] * multiplication[i][1] * multiplication[end][1]

    dp[start][end] = ans
    return ans

print(find_min(0, cases-1))
