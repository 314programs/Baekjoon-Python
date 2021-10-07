Word = input()
BreakLoop = False
while not BreakLoop:
    CharCount = 0
#Count Ws in the word
    for char in Word:
        if char == 'w':
            CharCount += 1
        else:
            break
#If the count is 0 or the length is too short, break
    if CharCount == 0 or len(Word) < 4:
        BreakLoop = True
        break
#Try and except to avoid index error  
    i = CharCount
    try:
#Checking the word by looking at count of Ws
        for a in range(i, i+CharCount):
            if Word[a] != 'o':
                BreakLoop = True

        for b in range(a+1, a+CharCount+1):
            if Word[b] != 'l':
                BreakLoop = True

        for c in range(b+1, b+CharCount+1):
            if Word[c] != 'f':
                BreakLoop = True
    except:
        BreakLoop = True
        break
#If the Word still has letters, repeat
    Word = Word[c+1:]
    
    if Word == '':
        break
    
if BreakLoop:
    print(0)
else:
    print(1)
