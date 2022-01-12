#I am still confused of orders so I decided to practice
VarNum = int(input())
Equation = input()
VarDict = {}
result = []

#Assign value to alphabet for later use
for i in range(65, 65+VarNum):
    VarDict[chr(i)] = int(input())

for token in Equation:
    if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        result.append(token)
    else:
      #Use the dictionary to assign values if they were not changed before
        a = result.pop()
        b = result.pop()
        
        if not isinstance(a, float) and not isinstance(a, int):
            a = VarDict[a]
        
        if not isinstance(b, float) and not isinstance(b, int):
            b = VarDict[b]
      #Evalulate for each case
        result.append(eval(str(b)+token+str(a)))
#Print till 2 decimals    
print('%.2f' % result[0])
