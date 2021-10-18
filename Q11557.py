TestCase = int(input())
for x in range(TestCase):
    ListLen = int(input())
    SchoolList = []
    for i in range(ListLen):
        Schoolname, age = map(str, input().split())
        SchoolList.append([Schoolname, int(age)])
    
    SchoolList.sort(key = lambda x: x[1])
    print(SchoolList[-1][0])
