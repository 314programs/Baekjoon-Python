TestCase = int(input())
for x in range(TestCase):
  StartX, StartY, EndX, EndY = map(int, input().split())
  PlanetNumber = int(input())
  Result = 0
  PlanetList = []
  for i in range(PlanetNumber):
    PlanetList.append(list(map(int, input().split()))) 

  for item in PlanetList:
    if (StartX - item[0])**2 + (StartY - item[1])**2 < item[2]**2 and (EndX - item[0])**2 + (EndY - item[1])**2 < item[2]**2:
      Result += 0
    elif (StartX - item[0])**2 + (StartY - item[1])**2 < item[2]**2 or (EndX - item[0])**2 + (EndY - item[1])**2 < item[2]**2:
      Result += 1

  print(Result)
