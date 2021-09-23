List1Len, List2Len = map(int, input().split())
List1 = list(map(int, input().split()))
List2 = list(map(int, input().split()))

TotalList = List1 + List2
TotalList.sort()

print(str(TotalList)[1:len(str(TotalList))-1].replace(',',''))
