Phase = str(input())
PelinList = []
#If the number is already a pelindrome, print its length and exit
if Phase[::-1] == Phase:
  print(len(Phase))
#If it is not pelindrome run a loop to make a list of pelindromes from the number
else:
  for i in range(1, len(Phase)+1):
    Temp = Phase[:i]
    PelinList.append(Temp + Temp[::-1])
    PelinList.append(Temp + Temp[:i-1][::-1])
#For items inside pelindrome list, check to see if item's front has the original phase inside
  ResultList = []

  for item in PelinList:
    if len(item) >= len(Phase):
      if item[:len(Phase)] == Phase:
        ResultList.append(len(item))

#Print the minimum from the lengths
  print(min(ResultList))
