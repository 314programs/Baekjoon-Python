#Take input, make a list from one to N
import collections 
ListLen, CaseCount = map(int, input().split())
AnswerList = list(map(int, input().split()))
NumList = collections.deque([int(i) for i in range(1,ListLen+1)])
Count = 0

#Loop for each item in case list
for item in AnswerList:
  while True:
    Mid = (len(NumList)//2)
#If first item is equal to the case item, break
    if item == NumList[0]:
      collections.deque.popleft(NumList)
      break
#Shift list to the right
    elif NumList.index(item) > Mid:
      Temp = collections.deque.pop(NumList)
      NumList.appendleft(Temp)
      Count += 1
#Shift list to the left
    else:
      Temp = collections.deque.popleft(NumList)
      NumList.append(Temp)
      Count += 1

print(Count)
