Channel = int(input())
BrokenNum = int(input())
if BrokenNum != 0:
  BrokenButton = list(map(int, input().split()))
  FunctionalButton = [int(i) for i in range(10) if i not in BrokenButton]
else:
  FunctionalButton = [int(i) for i in range(10)]

CurrentChannel = 100

result = [1000000, 0]
for a in range(1000000):
  Count = 0
  for char in str(a):
    if int(char) in FunctionalButton:
      Count += 1
  
  if Count == len(str(a)):
    if abs(Channel-a) < result[0]:
      result = [abs(Channel-a), a]

print(min(result[0]+len(str(result[1])), abs(CurrentChannel-Channel)))
