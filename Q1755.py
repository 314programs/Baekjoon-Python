Start, end = map(int, input().split())
NumDict = {}
#Make a dictionary that has a key of number and value of word
for i in range(Start, end+1):
    Word = ''
    for char in str(i):
        if char == '0':
            Word += 'zero '
        if char == '1':
            Word += 'one '
        if char == '2':
            Word += 'two '
        if char == '3':
            Word += 'three '
        if char == '4':
            Word += 'four '
        if char == '5':
            Word += 'five '
        if char == '6':
            Word += 'six '
        if char == '7':
            Word += 'seven '
        if char == '8':
            Word += 'eight '
        if char == '9':
            Word += 'nine '
            
    NumDict[i] = Word

#Sort it alphabetically and print
SortedList = sorted(NumDict.items(), key = lambda x:x[1])
Final = ''
Count = 0
for item in SortedList:
    Final += str(item[0]) + ' '
    Count += 1
    
    if Count == 10:
        print(Final.strip())
        Final = ''
        Count = 0
if Count > 0:
    print(Final.strip())
        
    
