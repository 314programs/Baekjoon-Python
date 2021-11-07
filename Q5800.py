from collections import deque

testCase = int(input())
for i in range(testCase):
    Class = list(map(int, input().split()))
    Length = Class[0]
    ClassSort = Class[1:]
    
    Max, Min = max(ClassSort), min(ClassSort)
    print('Class ' + str(i+1))
    ClassSort.sort(reverse = True)
    
    MaxDiff = 0
    for i in range(Length-1):
        MaxDiff = max(ClassSort[i] - ClassSort[i+1], MaxDiff)
    print('Max ' + str(Max) + ', ' + 'Min ' + str(Min) + ', ' + 'Largest gap ' + str(MaxDiff))
