from collections import deque

equation = input()
NumList = deque([])
SignList = deque([])

#Make list of number and signs
Temp = ''
for char in equation:
    if char == '-':
        if len(Temp) != 0:
            NumList.append(int(Temp))
        SignList.append('-')
        Temp = ''
    elif char == '+':
        if len(Temp) != 0:
            NumList.append(int(Temp))
        SignList.append('+')
        Temp = ''
    else:
        Temp += char
        
NumList.append(int(Temp))

if len(NumList) != len(SignList):
    SignList.appendleft('+')

#Use the list of numbers and signs to sum up the result
MinusOn = False
Result = 0

for i in range(len(NumList)):
    if SignList[i] == '-':
        MinusOn = True
        
    if MinusOn:
        Result -= NumList[i]
    else:
        Result += NumList[i]
        
        
print(Result) 
    

