CaseCount = int(input())
for b in range(CaseCount):
  inputNum = int(input())
  KoongList = [1,1,2,4]

#Save our values in the list for later usage
  for i in range(4, inputNum+1):
    KoongList.append(KoongList[i-1]+KoongList[i-2]+KoongList[i-3]+KoongList[i-4])
    
  print(KoongList[inputNum])

