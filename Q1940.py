ListLen = int(input())
NeededNum = int(input())
NumList = list(map(int, input().split()))
NumList.sort()
print(NumList)
Count = 0

start = ListLen-2
end = ListLen-1

while end != start:
    print(NumList[start], NumList[end])
    if NumList[start] + NumList[end] == NeededNum:
        Count += 1

    if NumList[start] + NumList[end] > NeededNum and start > 0:
        start -= 1
    else:
        if end > 1:
            end -= 1  
        if end > 1:
            start = end -1 
    
print(Count)
