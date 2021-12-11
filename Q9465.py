#I need to do more DP, I had to get help from tutorial
CaseCount = int(input())
for v in range(CaseCount):
    Width = int(input())
    Sticker = []
    
    for i in range(2):
        Sticker.append(list(map(int, input().split())))
#Set up list for Dynamic programming
    ScoreList = [[0,0,0]]
    for i in range(Width):
        ScoreList.append([0,0,0])
    
    ScoreList[1][1] = Sticker[0][0]
    ScoreList[1][2] = Sticker[1][0]
#Third vairable in the list to measure if a zig-zag should be used or a skip
    for i in range(2,Width+1):
        ScoreList[i-1][0] = max(ScoreList[i-2][1], ScoreList[i-2][2])
        ScoreList[i][1] = max(ScoreList[i-1][0], ScoreList[i-1][2]) + Sticker[0][i-1]
        ScoreList[i][2] = max(ScoreList[i-1][0], ScoreList[i-1][1]) + Sticker[1][i-1]
        
    print(max(ScoreList[-1][1], ScoreList[-1][2]))
