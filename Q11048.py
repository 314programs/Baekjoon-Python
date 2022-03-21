#Graph DP...
import sys
input = sys.stdin.readline

Height, Width = map(int, input().split())
Graph = [list(map(int, input().split())) for v in range(Height)]
DP = [[0 for v in range(Width + 1)] for i in range(Height+1)]

for h in range(1, Height+1):
    for w in range(1, Width+1):
        DP[h][w] = max(DP[h][w-1], DP[h-1][w], DP[h-1][w-1]) + Graph[h-1][w-1]
print(DP[Height][Width])
