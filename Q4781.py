while True:
    Item, MaxCost = map(float, input().split())
    #+0.5 for accurate integer conversion
    MaxCost = int(MaxCost*100 + 0.5)
    
    if int(Item) == 0 and int(MaxCost) == 0:
        break
    
    DP = [0 for v in range(MaxCost+1)]

    for i in range(int(Item)):
        Current_Cal, Current_Cost = map(float, input().split())
        Current_Cal = int(Current_Cal)
        Current_Cost = int(Current_Cost*100 + 0.5)
        
        #Can just use 1 DP list by using max() function
        for c in range(Current_Cost, MaxCost+1):
          #Select maximum from current value and current cal + maximum value from the money left
            DP[c] = max(DP[c], DP[c-Current_Cost] + Current_Cal)
    print(DP[MaxCost])
