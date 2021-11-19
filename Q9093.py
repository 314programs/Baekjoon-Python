TestCase = int(input())
for i in range(TestCase):
    sentence = input()
    SList = sentence.split()
    for i in range(len(SList)):
        SList[i] = SList[i][::-1]
    print(' '.join(SList))
