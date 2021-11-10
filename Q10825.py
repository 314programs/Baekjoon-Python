CaseCount = int(input())
NameList = []
for i in range(CaseCount):
    Name, Language, English, Math = map(str, input().split())
    NameList.append([Name, int(Language), int(English), int(Math)])

NameList.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]), reverse = False)

for item in NameList:
    print(item[0])
