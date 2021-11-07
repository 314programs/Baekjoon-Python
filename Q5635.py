CaseCount = int(input())
Dict = {}
for i in range(CaseCount):
    temp = list(map(str, input().split()))
    Dict[temp[0]] = [int(temp[1]),int(temp[2]),int(temp[3])]

result = sorted(Dict.items(), key = lambda x:(x[1][2], x[1][1], x[1][0]))
print(result[-1][0])
print(result[0][0])
