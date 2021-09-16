import sys
#Set up
PhaseCount, WordCount = map(int, sys.stdin.readline().rstrip().split())
#Speed up code using list list comprehension
PhaseList = {sys.stdin.readline().rstrip() for i in range(PhaseCount)}
Count = 0
#Find and print count
for i in range(WordCount):
  if sys.stdin.readline().rstrip() in PhaseList:
    Count += 1

sys.stdout.write(str(Count)+'\n')
