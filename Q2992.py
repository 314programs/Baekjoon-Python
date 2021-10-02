Number = input()
i = int(Number)+1

#Make a list that contains count of numbers
NumCountList = []
for x in range(10):
  NumCountList.append([x, 0])

for char in Number:
  NumCountList[int(char)][1] += 1


while True:
#Make a list that contains count of but for i
  iCountList = []

  for a in range(10):
    iCountList.append([a, 0])

  for char in str(i):
    iCountList[int(char)][1] += 1
#Compare lists
  if iCountList == NumCountList:
    print(i)
    break
#If the length goes over, it cannot be made, so break and print 0
  if len(str(i)) > len(Number):
    print(0)
    break

  i += 1
