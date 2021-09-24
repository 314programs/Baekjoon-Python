Phase = str(input())
PelinList = []
if Phase[::-1] == Phase:
  print(len(Phase))

else:
  for i in range(1, len(Phase)+1):
    Temp = Phase[:i]
    PelinList.append(Temp + Temp[::-1])
    PelinList.append(Temp + Temp[:i-1][::-1])

  ResultList = []

  for item in PelinList:
    if len(item) >= len(Phase):
      if item[:len(Phase)] == Phase:
        ResultList.append(len(item))


  print(min(ResultList))
