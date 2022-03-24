#Try all 1,2,3 adding questions in the future
#Still slightly confused on the methods
import sys
input = sys.stdin.readline

testcase = int(input())
for case in range(testcase):
    num = int(input())
    DP = [0 for v in range(num+1)]
    DP[0] = 1

    for j in range(1, 4):
        for i in range(1, num+1):
            if i - j >= 0:
                DP[i] += DP[i-j]
    print(DP[num])
