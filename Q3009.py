XList = []
YList = []

for i in range(3):
    X, Y = map(int, input().split())
    XList.append(X)
    YList.append(Y)

Result = ''

for item in XList:
    if XList.count(item) == 1:
        Result += str(item) + ' '
        break
for item in YList:
    if YList.count(item) == 1:
        Result += str(item)
        break
print(Result)


