SCV_num = int(input())
SCV_list = list(map(int, input().split()))
while len(SCV_list) < 3:
    SCV_list.append(0)

#I wrote [[-1] * 61] * 61, spent hour trying to find whats wrong
dp = [[[-1]*61 for j in range(61)] for i in range(61)]

#All permutations
p = [[1, 3, 9],[1, 9, 3],[3, 1, 9], [3, 9, 1],[9, 1, 3],[9, 3, 1]]

def solve(SCV1_, SCV2_, SCV3_):
    if SCV1_ < 0: return solve(0, SCV2_, SCV3_)
    if SCV2_ < 0: return solve(SCV1_, 0, SCV3_)
    if SCV3_ < 0: return solve(SCV1_, SCV2_, 0)

    if SCV1_ == 0 and SCV2_ == 0 and SCV3_ == 0:
        return 0

    ans = dp[SCV1_][SCV2_][SCV3_]
    
    #Use memorised value if possible
    if ans != -1:
        return ans

    ans = float('inf')

    for i in range(6):
        ans = min(ans, solve(SCV1_ - p[i][0], SCV2_ - p[i][1], SCV3_ - p[i][2]))

    ans += 1
    dp[SCV1_][SCV2_][SCV3_] = ans
    return dp[SCV1_][SCV2_][SCV3_]

print(solve(SCV_list[0], SCV_list[1], SCV_list[2]))
