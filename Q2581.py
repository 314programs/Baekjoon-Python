StartNum = int(input())
EndNum = int(input())
ResultsList = []

#Checks if number is prime
def Prime(num):
  for i in range(2, int(num**0.5) + 1):
    if num%i == 0:
      return False
  
  if num != 1:
    return True

for i in range(StartNum, EndNum+1):
  if Prime(i):
    ResultsList.append(i)

#Prints according to list length
if len(ResultsList) != 0:
  print(sum(ResultsList))
  print(ResultsList[0])
else:
  print('-1')
