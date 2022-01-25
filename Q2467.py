#Use binary search similar to 2470.py
#It can be passed with the same code as 2470, but I updated the code 
ListLen = int(input())
NumList = list(map(int, input().split()))
MinNum = float('inf')
MinVals = [0,0]
NumList.sort()

start = 0
end = ListLen - 1

while start < end:
    CurrentVal = NumList[start] + NumList[end]
    if abs(CurrentVal) < MinNum:
        MinNum = abs(CurrentVal)
        MinVals = [NumList[start], NumList[end]]
        
    if CurrentVal < 0:
        start += 1
    else:
        end -= 1

print(MinVals[0], MinVals[1])
