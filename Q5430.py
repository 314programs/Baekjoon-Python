import collections
import sys
#Get input
CaseCount = int(sys.stdin.readline().rstrip())
for x in range(CaseCount):
  Commend = sys.stdin.readline().rstrip()
  ListLen = int(sys.stdin.readline().rstrip())
  ListString = sys.stdin.readline().rstrip()[1:-1]
  if ListLen > 0:
    TheList = collections.deque(list(map(int, ListString.split(sep = ','))))
  else:
    TheList = []
  Results = []
  RCount = 0
  Error = False
#Count R instead of reversing the list everytime
  for i in range(len(Commend)):
    if len(TheList) == 0 and Commend[i] == 'D':
      Error = True
      break
    if Commend[i] == 'R':
      RCount += 1

    if RCount == 0 or RCount%2==0:
      if Commend[i] == 'D':
        TheList.popleft()
    else:
      if Commend[i] == 'D':
        TheList.pop()

  if not Error:
    if RCount == 0 or RCount%2==0:
      for i in range(len(TheList)):
        Results.append(TheList[i])
    else:
      for i in range(len(TheList)-1, -1, -1):
        Results.append(TheList[i])
    sys.stdout.write(str(Results).replace(' ', '') + '\n')
  else:
    sys.stdout.write('error' + '\n')
