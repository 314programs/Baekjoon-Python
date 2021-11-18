import math
while True:
    try:
        CuponNum, ChickenNeeded = map(int, input().split())
    except:
        break
        
    ChickenNum = 0
    Total = 0

    while True:
        Total += CuponNum
        ChickenNum += CuponNum
        CuponNum = math.floor(ChickenNum//ChickenNeeded)
        ChickenNum = (ChickenNum%ChickenNeeded)
        
        if CuponNum == 0:
            print(Total)
            break
            
        
        print(ChickenNum, CuponNum, Total)
        

        
