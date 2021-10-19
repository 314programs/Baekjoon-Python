#Get input
import sys
input = sys.stdin.readline

ListLen, NumNeeded = map(int, input().split())
NumList = list(map(int, input().split()))

Count = 0
#Use two pointer algorithm to find correct start and end points
for start in range(ListLen):
    end = start
    Addition = NumList[start]
    while True:
        if end >= ListLen: 
            break
        if end != start:
#Instead of using sum() just add it to a variable to save time
            Addition += NumList[end]
        
        if Addition == NumNeeded:
            Count += 1
        end += 1
            
print(Count) 
