#Instead of slicing lists, use a simple formula to save time + memory
NeededNum = int(input())
Count = 0

start = NeededNum-2
end = NeededNum-1

while end >= start:
    Temp = int(0.5 * (end - start+1) * (end + start)) 
    if Temp == NeededNum:
        Count += 1

    if Temp < NeededNum and start > 0:
        start -= 1
    else:
        end -= 1        
    
print(Count+1)
