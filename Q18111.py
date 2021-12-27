import sys
import collections
def FindHeightandTime(MaxHeight, Minheight, Blocks, BlockMap):
  TotalList = collections.deque([])
  for i in range(Minheight, MaxHeight+1):
    Remove_Diff_Value = 0
    Add_Diff_Value = 0
    TotalValue = 0

    #Checking block diff to current floor
    for x in BlockMap:
      if i-x > 0:
        Add_Diff_Value += i-x

      elif i-x < 0:
        Remove_Diff_Value += abs(i-x)
    

    #If blocks + removing value which will make total blocks is bigger than blocks needed for placing, then calculate total Value
    if Add_Diff_Value <= Remove_Diff_Value + Blocks:
      TotalValue = Add_Diff_Value + (Remove_Diff_Value*2)
      TotalList.append([TotalValue,i])

  TotalList = sorted(TotalList, key = lambda x: (x[0], -x[1]))
  return str(TotalList[0][0]) + ' ' + str(TotalList[0][1])

TheList = collections.deque([])
Height, Width, BlockNum = map(int, sys.stdin.readline().split())
for i in range(Height):
  Temp = list(map(int, sys.stdin.readline().split()))
  for item in Temp:
    TheList.append(item)

sys.stdout.write(FindHeightandTime(max(TheList), min(TheList), BlockNum, TheList))
    
