MaxWord = ''
Run = True
while Run:
    Sentence = input()
    CleanSentence = ''
    theList = list(map(str, Sentence))

    for i in range(len(theList)):
        if theList[i].isalpha() or theList[i] == '-' or theList[i] == ' ':
            CleanSentence += theList[i]
            
    CleanList = list(map(str, CleanSentence.split()))
    
    for item in CleanList:
        if item == 'E-N-D':
            print(MaxWord.lower())
            Run = False
            break
        if len(MaxWord) < len(item):
            MaxWord = item
