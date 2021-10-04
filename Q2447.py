import math
import sys

#Preloaded list and variables
Input = int(input())
Num = int(math.log((Input+1),3))
StarLen=1
StarList = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]

for x in range(Num):
  TempList = []
  InnerList = []
#Repeat for the length and the width of the list
  for a in range(3**StarLen):
    for b in range(3**StarLen):
#This if loop checks if it is empty space or not, if it is it will append empty spaces
#If it is not, it will append items from the generated StarList according to a and b
      if a > (3**(StarLen-1)-1) and a < ((3**(StarLen-1)*2)) and b > (3**(StarLen-1)-1) and b < ((3**(StarLen-1)*2)):
        InnerList.append(' ')
      else:
        InnerList.append(StarList[a%3**(StarLen-1)][b%3**(StarLen-1)])

    TempList.append(InnerList)
    InnerList = []
#Update the starlist
  StarList = TempList
  StarLen += 1

for item in TempList:
  print(''.join(item))
