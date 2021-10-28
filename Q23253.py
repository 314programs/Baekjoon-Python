import sys
input = sys.stdin.readline

BookNum, PileNum = map(int, input().split())
Pile = []
MaxPileLen = 0

for i in range(PileNum):
    MaxPileLen = max(MaxPileLen, int(input()))
    Pile.append(list(map(int, input().split())))

PrintAnswer = True

for item in Pile:
    
    if len(item) != 0:
        for i in range(len(item)-1):
            if item[i] > item[i+1]:
                continue
            else:
                PrintAnswer = False
        
if PrintAnswer:
    print('Yes')
else:
    print('No')

    
