Listlen = int(input())
TheList = list(map(int, input().split()))
ResultList = []
i = 0
while i <= (Listlen-1):
    Number = TheList[i]
    ResultList.append(str(Number))
    i += Number

print(' '.join(ResultList))
    
