import sys
input = sys.stdin.readline
#Get input and declare variables
Dimension, TestCase = map(int, input().split())
Square = []

for a in range(Dimension):
    Square.append(list(map(int, input().split())))

TestCaseList = []
for b in range(TestCase):
    TestCaseList.append(list(map(int, input().split())))
    
SquareSum = []

#Get sum of each row
for item in Square:
    Temp = [0]
    for numbers in item:
        Temp.append(Temp[-1] + numbers)
    SquareSum.append(Temp)

#Use the sum of the rows and subtract to get the result
for case in TestCaseList:
    result = 0
    for i in range(case[0],case[2]+1):
        result += SquareSum[i-1][case[3]]-SquareSum[i-1][case[1]-1]
        
    sys.stdout.write(str(result)+'\n')
