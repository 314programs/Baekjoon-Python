Listlen = int(input())
StairList = [0]
for i in range(Listlen):
    StairList.append(int(input()))

if Listlen == 1:
    print(StairList[-1])
else:
    ResultList = [[0,0,0], [0,0,0], [0,0,0]]
#Initialize values
    ResultList[1][1] = StairList[1]
    ResultList[1][2] = 0
    ResultList[2][1] = StairList[2]
    ResultList[2][2] = StairList[2] + StairList[1]
#Use dynamic programming to find the maximum score
#The ResultList's indexes indicate the stares taken before the current stair
    for i in range(3, Listlen+1):
        ResultList.append([0,0,0])
        ResultList[i][1] = max(ResultList[i-2][1], ResultList[i-2][2]) + StairList[i]
        ResultList[i][2] = ResultList[i-1][1] + StairList[i]

    print(max(ResultList[-1]))

