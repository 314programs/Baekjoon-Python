NeededNum = int(input())
NumList = [v for v in range(1,NeededNum)]
Count = 0

start = NeededNum-2
end = NeededNum-1

while end != start:
    if sum(NumList[start:end]) == NeededNum:
        Count += 1

    if sum(NumList[start:end]) < NeededNum and start > 0:
        start -= 1
    else:
        end -= 1        
    
print(Count+1)
