#Set up ant list
Group1Len, Group2Len = map(int, input().split())
if Group1Len > 0: Group1 = [char for char in input()][::-1]
else: Group1 = []
if Group2Len > 0: Group2 = [char for char in input()]
else: Group2 = []
    
Time = int(input())

TotalAnt = []
for item in Group1: TotalAnt.append([item, 'right'])
for item in Group2: TotalAnt.append([item, 'left'])

#Check if ants are bumping into each other
for i in range(Time):
    x = 0
    while x + 1 <= Group1Len + Group2Len -1:
        if TotalAnt[x][1] == 'right' and TotalAnt[x+1][1] == 'left':
            Right = TotalAnt[x]
            Left = TotalAnt[x+1]
            
            TotalAnt[x] = Left
            TotalAnt[x+1] = Right
            x += 2
        else:
            x += 1
            
#Print        
Result = ''
for item in TotalAnt: Result += item[0]      
print(Result)
