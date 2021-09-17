#Import and input
import sys
ListLen = int(sys.stdin.readline())
InputList = list(map(int, sys.stdin.readline().split()))
CountList = [0]*(1000001)
SortedList = []
Number = int(sys.stdin.readline())
count = 0

#Binary Search
def SearchBinary(Answer):
  Minimum = 0
  Maximum = len(SortedList) - 1

  while Minimum <= Maximum:
    Mid = (Minimum+Maximum)//2

    if SortedList[Mid] == Answer:
      return 1
    
    else:
      if SortedList[Mid] < Answer:
        Minimum = Mid + 1
      elif SortedList[Mid] > Answer:
        Maximum = Mid - 1
    
  return 0

#Counting sort
for i in range(ListLen):
  CountList[InputList[i]] += 1

for i in range(1000001):
  for a in range(CountList[i]):
    SortedList.append(i)

for item in SortedList:
  Temp = Number-item
  if Temp < item:
    count += SearchBinary(Temp)

sys.stdout.write(str(count) + '\n')
