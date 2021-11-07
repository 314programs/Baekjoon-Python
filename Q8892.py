TestCase = int(input())

def Pelin(length):
    for a in range(length):
        for b in range(length):
            if a != b and (WordList[a] + WordList[b])[::-1] == (WordList[a] + WordList[b]):
                return WordList[a] + WordList[b]
    return 0
#Just use bruteforce
for i in range(TestCase):
    ListLen = int(input())
    WordList = []
    for v in range(ListLen):
        WordList.append(input())
    print(Pelin(ListLen))
