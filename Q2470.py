import sys
input = sys.stdin.readline

ListLen = int(input())
NumList = list(map(int, input().split()))
MinNum = 2000000001
MinList = [0,0]
NumList.sort()

#Set up starting and ending potions
start = 0
end = ListLen-1

#Two pointer algorithm
while True:
#Save values if current sum is less than minimum sum
    if abs(NumList[end] + NumList[start]) < MinNum:
        MinNum = abs(NumList[end] + NumList[start])
        MinList[0] = start
        MinList[1] = end
#If Sum is smaller than 0, start += 1 to increase it
#Else decrease the end
    if NumList[end] + NumList[start] < 0 and start < ListLen-1:
        start += 1
    else:
        if end > 1:
            end -= 1
        else:
            break
        
    if end == start:
        break
            
#Sort and print   
ResultList = [NumList[MinList[0]], NumList[MinList[1]]]
ResultList.sort()
print(ResultList[0], ResultList[1])
