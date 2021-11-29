OddList = []
for i in range(7):
    num = int(input())
    if num%2 != 0:
        OddList.append(num)
if OddList:
    print(sum(OddList))
    print(min(OddList))
else:
    print('-1')
