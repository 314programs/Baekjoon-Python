Lower = int(input())
Higher = int(input())
SquareList = []

for i in range(Lower, Higher+1):
    if i**0.5 == int(i**0.5):
        SquareList.append(i)
        
if len(SquareList) != 0:
    print(sum(SquareList))
    print(min(SquareList))
else:
    print('-1')
