Length, Wanted_Num = map(int, input().split())
NumList = list(map(int, input().split()))
TotalList = [0]
Min_Val = float('inf')

#Make total list so that I don't have to use sum() each time and cause a timeout
for i in range(Length):
    TotalList.append(TotalList[-1] + NumList[i])
    
Start = 0
End = 0

#Another two pointer algorithm
while True:
    Sum = TotalList[End] - TotalList[Start]
    if Sum < Wanted_Num:
        End += 1
        
    else:
        Min_Val = min(Min_Val, End-Start)
        Start += 1
    
    if Start == Length+1 or End == Length+1:
        break

if Min_Val == float('inf'):
    print(0)
else:
    print(Min_Val)
