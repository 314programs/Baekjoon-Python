StudentCount = int(input())
StudentList = []
for i in range(StudentCount):
    StudentList.append(list(map(int, input().split())))
ClassList = []

for i in range(5):
    Temp = []
    for item in StudentList:
        Temp.append(item[i])
    ClassList.append(Temp)

ResultList = []

StudentNum = 1
for x in range(StudentCount):
    Result = set([])
    for i in range(5):
        for h in range(StudentCount):
            if ClassList[i][h] == StudentList[x][i]:
                Result.add(h)
    
    ResultList.append([len(Result)-1, StudentNum])
    StudentNum += 1
    
    
ResultList.sort(key = lambda x: (x[0], -x[1]), reverse = True)
print(ResultList[0][1])
        
