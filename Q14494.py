#To recap about dynamics
#Since there are so many dynamic questions in class 5, I thought I needed a quick recap
import sys
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())

DP = [[0 for v in range(n+1)] for v in range(m+1)]
DP[1][1] = 1

def recursion(x_, y_):
    if x_ <= 0 or y_ <= 0:
        return 0
    elif DP[y_][x_] != 0:
        return DP[y_][x_]%(10**9 + 7)
    else:
        DP[y_][x_] = recursion(x_-1, y_) + recursion(x_, y_-1) + recursion(x_-1, y_-1)
        return DP[y_][x_]%(10**9 + 7)

recursion(n,m)

print(DP[m][n]%(10**9 + 7))
