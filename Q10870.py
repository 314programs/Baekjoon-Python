Number = int(input())
theList = [0,1]
for i in range(Number-1):
  theList.append(theList[i] + theList[i+1])

print(theList[Number])
