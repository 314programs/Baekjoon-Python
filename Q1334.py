#Since it is the next pelindrome number, add one to the input
InputNum = str(int(input()) + 1)
Half = len(InputNum)//2

#If the input has length of 1, print it
if len(InputNum) == 1:
  print(InputNum)

#Else, calculate the first half and the second half of the number depending on its length, even or odd.
else:
  if len(InputNum)%2 != 0:
    StartNum = int(InputNum[0:Half+1])
    EndNum = int(InputNum[Half+1:len(InputNum)])

  else:
    #No mid
    StartNum = int(InputNum[0:Half])
    EndNum = int(InputNum[Half:len(InputNum)])
#If the second half of numbers are smaller than the first half reversed, just print first half + first half reversed
  if int(str(StartNum)[0:Half][::-1]) >= int(str(EndNum)):
    print(str(StartNum)+str(StartNum)[0:Half][::-1])
#If not, add one to the first half and print first half + first half reversed
  else:
    StartNum += 1
    print(str(StartNum)+str(StartNum)[0:Half][::-1])
