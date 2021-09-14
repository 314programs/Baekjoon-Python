import sys
#Take input
NumCount, SumCount = map(int, sys.stdin.readline().split())
NumList = list(map(int, sys.stdin.readline().split()))

Sums = [0]
#Make a list of added values
for i in range(NumCount):
  Sums.append(Sums[-1] + NumList[i])
#Use the list of added values to calculate the sum
for i in range(SumCount):
  Start, End = map(int, sys.stdin.readline().split())
  sys.stdout.write(str(Sums[End] - Sums[Start-1]) + '\n')
