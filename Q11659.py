import sys

NumCount, SumCount = map(int, sys.stdin.readline().split())
NumList = list(map(int, sys.stdin.readline().split()))

Sums = [0]

for i in range(NumCount):
  Sums.append(Sums[-1] + NumList[i])

for i in range(SumCount):
  Start, End = map(int, sys.stdin.readline().split())
  sys.stdout.write(str(Sums[End] - Sums[Start-1]) + '\n')
