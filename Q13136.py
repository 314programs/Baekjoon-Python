import sys
import math
input = sys.stdin.readline

R, C, D = map(float, input().split())
print(int(math.ceil(R/D) * math.ceil(C/D)))
