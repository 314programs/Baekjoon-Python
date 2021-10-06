WordListLen = int(input())
Word = input()
Count = 0
WordList = []
for i in range(WordListLen-1):
    WordList.append(input())

for item in WordList:
    WarningCount = 0
    length = abs(len(item)-len(Word))
    
#Put it as a set to avoid repetition and count characters
    for char in set(Word):
        WarningCount += abs(Word.count(char) - item.count(char))
        item = item.replace(char, '')
#Since the characters in the original version was counted, we can measure the length of the word to see leftovers
    WarningCount += len(item)

    if WarningCount <= 2 and length < 2:
        Count += 1

print(Count)
        

