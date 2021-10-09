import sys
input = sys.stdin.readline

#Make a list beforehand to save time, only divide by prime numbers as well that is updated throughout the loop
PrimeList = [2,3]
for i in range(5, 246913):
    Count = 0
    for item in PrimeList:
        if i%item == 0:
            Count = 1
            break
    if Count == 0:
        PrimeList.append(i)

#Take input and print results accordingly
theinput = 1
while True:
    theinput = int(input())
    if theinput == 0:
        break
    Count = 0
    for item in PrimeList:
        if item > theinput and item <= theinput*2:
            Count += 1
    sys.stdout.write(str(Count)+'\n')

            

