RingNum = int(input())
RingList = list(map(int, input().split()))

for i in range(1,RingNum):
  TopFrac = RingList[0]
  BottomFrac = RingList[i]

  if TopFrac/BottomFrac == int(TopFrac/BottomFrac):
    print(str(int(TopFrac/BottomFrac)) + '/1')
  
  else:
    DivisionNum = 1
    for z in range(1,TopFrac+1):
      if TopFrac%z == 0 and BottomFrac%z == 0 and z > DivisionNum:
        DivisionNum = z

    TopFrac = int(RingList[0]/DivisionNum)
    BottomFrac = int(BottomFrac/DivisionNum)
    print(str(TopFrac) + '/' + str(BottomFrac))
  
