import sys
input = sys.stdin.readline

#Get input
coin_type_num, wanted_value = map(int, input().split())
types = [int(input()) for v in range(coin_type_num)]
DP = [0 for v in range(wanted_value + 1)]
DP[0] = 1

for item in types:
    for i in range(1, wanted_value+1):
        #Use previous values if possible
        if i - item >= 0:
            DP[i] += DP[i-item]

print(DP[wanted_value])
