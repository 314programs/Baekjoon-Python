#Set up lists of functional buttons
Channel = int(input())
BrokenNum = int(input())
if BrokenNum != 0:
  BrokenButton = list(map(int, input().split()))
  FunctionalButton = [int(i) for i in range(10) if i not in BrokenButton]
else:
  FunctionalButton = [int(i) for i in range(10)]

CurrentChannel = 100

#Because speed is not needed, loop it until the maximum point to get the answer.
result = [1000000, 0]
for a in range(1000000):
  Count = 0
#Checking if the number can be made with functional buttons
  for char in str(a):
    if int(char) in FunctionalButton:
      Count += 1
#Checking if the current result is better(Smaller) than the previous
  if Count == len(str(a)):
    if abs(Channel-a) < result[0]:
      result = [abs(Channel-a), a]
#Print minimum between pressing arrow buttons and number buttons to pressing only arrow buttons
print(min(result[0]+len(str(result[1])), abs(CurrentChannel-Channel)))
