StarList = ['*']
StarCount = 1
num = int(input())
for i in range(num-1):
    StarCount += 4
    Temp = []
    
#The first 3 lines and the last 3 lines has a pattern which can be used
    Temp.append('*'*StarCount)
    Temp.append('*' + ' '*(StarCount - 1))
    Temp.append('*' + ' ' + StarList[0] + '**')
    
#Use the previously stored stars to make another spiral inside
    if len(StarList) != 1:
        for v in range(StarCount -4):
            Temp.append('*' + ' ' + StarList[v+1] + ' ' + '*')
    else:
        Temp.append('*' + ' ' + StarList[0] + ' ' + '*')
    
    Temp.append('*' + ' ' + StarList[-1] + ' ' +'*')
    Temp.append('*' + ' '*(StarCount - 2) + '*')
    Temp.append('*'*StarCount)
    
    StarList = Temp
    
for item in StarList:
    print(item.strip())
