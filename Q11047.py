CoinNum, CoinValue = map(int, input().split())
CoinList = []
for i in range(CoinNum):
    CoinList.append(int(input()))

#Take input and sort in in descending order
CoinList.sort(reverse = True)
Ans = 0

#If one of the values in the coinlist is smallr or equal to coin value, divide it (//) since it will automatically floor
#Subtract it from the coin value and repeat
for item in CoinList:
    if CoinValue >= item:
        Ans += CoinValue//item
        CoinValue -= item*(CoinValue//item)
    
print(Ans)
    
    
