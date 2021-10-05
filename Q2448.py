import sys
import math

Number = int(sys.stdin.readline())
Pow = int(math.log((Number//3), 2))

#Triangle list, since it will be used over and over again
StarList = ['  *  ',' * * ','*****']
#Set this in case the input is 3
ResultList = StarList

for x in range(Pow):

    ResultList = []
    TempList = []
#2 bottom triangles
    for i in range(3*(2**x)):
        TempList.append(StarList[i]+' '+StarList[i])
#Top triangle
    for item in StarList:
        ResultList.append((' '*(3*(2**x)) + item + (' '*(3*(2**x)))))
#Combine the bottom and top list together
    for item in TempList:
        ResultList.append(item)

#Update the triangle list for the next loop
    StarList = ResultList

#Print
for item in ResultList:
    sys.stdout.write(''.join(item) + '\n')
    
