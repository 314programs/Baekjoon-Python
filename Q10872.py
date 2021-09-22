num = int(input())
NumberList = [1]
for i in range(1,num+1):
  NumberList.append(NumberList[-1]*i)

print(NumberList[-1])
