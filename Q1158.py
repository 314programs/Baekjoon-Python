ListLen, Movement = map(int, input().split())
TheList = [v for v in range(1,ListLen+1)]
ResultList = []
i = Movement - 1

while TheList:
    while i > len(TheList)-1: 
        i -= len(TheList)
        
    Temp = TheList.pop(i)
    i += Movement-1
    
    ResultList.append(str(Temp))
    
print('<'+', '.join(ResultList)+'>')
