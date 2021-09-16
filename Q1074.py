#Get variables and input
import sys
DimensionPower, Row, Column = map(int, sys.stdin.readline().split())
Count = []

#Declare a function that splits the map into 4 pieces depending on the middle line.
#According to which place, add values to the list, and repeat the function until the dimension is 0.
def Division(Dimension, TheRow, TheColumn):
  DivideSection = Dimension//2
  if Dimension == 0:
    return 

  if TheRow < DivideSection and TheColumn < DivideSection:
    Division(DivideSection, TheRow, TheColumn)
  elif TheRow < DivideSection and TheColumn >= DivideSection:
    Count.append(DivideSection**2)
    Division(DivideSection, TheRow, TheColumn-DivideSection)
  elif TheRow >= DivideSection and TheColumn < DivideSection:
    Count.append((DivideSection**2)*2)
    Division(DivideSection, TheRow-DivideSection, TheColumn)
  elif TheRow >= DivideSection and TheColumn >= DivideSection:
    Count.append((DivideSection**2)*3)
    Division(DivideSection, TheRow-DivideSection, TheColumn-DivideSection)

#Use function and print values
Division(2**DimensionPower, Row, Column)
sys.stdout.write(str(sum(Count)) + '\n')
