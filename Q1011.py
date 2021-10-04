CaseCount = int(input())
#This question has a pattern of 1, 121, 12321, 1234321...
#Its total sum is a square of the number in the middle 
for x in range(CaseCount):
  Start, end = map(int, input().split())
  Distance = end-Start
#Calculate the nearest square
  PowerVal = min((int(Distance**0.5))**2, (int(Distance**0.5)+1)**2)
  Needed = Distance-PowerVal

#If more distance is needed, subtract the middle number(biggest number) until it is smaller or equal to 0
#We can subtract the middle number since smallest amount of movement is needed
  if Needed > 0:
    Count = 0

    while Needed > 0:
      Count += 1
      Needed -= int(PowerVal**0.5)
      
    print(Count + 1 + (2*(int(PowerVal**0.5)-1)))
  else:
    print(1 + (2*(int(PowerVal**0.5)-1)))
