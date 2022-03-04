#Solved using BFS
from collections import deque

num = int(input())
numList =['' for v in range(num+1)]
queue = deque([num])
numList[num] = str(num)

#Repeat until 1 is empty
while numList[1] == '':
    Temp = queue.popleft()
    
    #Only change the value when the length of operations taken was less or the value was empty
    if Temp%3 == 0 and (numList[Temp//3].count(' ') > numList[Temp].count(' ')+1 or numList[Temp//3] == ''):
        numList[Temp//3] = numList[Temp] + ' ' + str(Temp//3)
        queue.append(Temp//3)
        

    if Temp%2 == 0 and (numList[Temp//2].count(' ') > numList[Temp].count(' ')+1 or numList[Temp//2] == ''):
        numList[Temp//2] = numList[Temp] + ' ' + str(Temp//2)
        queue.append(Temp//2)
        
    
    if Temp-1 > 0 and (numList[Temp-1].count(' ') > numList[Temp].count(' ')+1 or numList[Temp-1] == ''):
        numList[Temp-1] = numList[Temp] + ' ' + str(Temp-1)
        queue.append(Temp-1)

#Print output
print(numList[1].count(' '))
print(numList[1])
