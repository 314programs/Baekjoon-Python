#Input and set up
Start, End = map(int, input().split())
NumList = []
#For stopping the loop
Alarm = False
#Loop to make a list
for a in range(1,End+1):
  for b in range(a):
    NumList.append(a)
    if len(NumList) >= End:
      Alarm = True
      break
  if Alarm:
    break

#Since speed is not needed, sum is used
print(sum(NumList[Start-1:End]))
