import sys
Dimension = int(sys.stdin.readline().rstrip())
ListMap = []
Results = []

for i in range(Dimension):
  ListMap.append(list(char for char in sys.stdin.readline().rstrip()))

def SplitAndCheck(TheDimension, MappingList, ResultList):
  Division = TheDimension//2

  for i in range(0,2):
    if MappingList.count([str(i)]*TheDimension) == TheDimension:
      ResultList.append(i)
      return
  
  ResultList.append('(')
  for y in range(0, TheDimension, Division):
    for x in range(0, TheDimension, Division):
      Temp = []
      for r in range(y, y+Division):
        Temp.append(MappingList[r][x:x+Division])
      SplitAndCheck(Division, Temp, ResultList)
  ResultList.append(')')

SplitAndCheck(Dimension, ListMap, Results)
ResultString = ''
for item in Results:
  ResultString += str(item)

sys.stdout.write(ResultString)