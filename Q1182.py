#Practicing backtracking
Length, Num = map(int, input().split())
NumList = list(map(int, input().split()))
Visited = [0 for v in range(Length)]

Count = 0

def MakeNums(NumLen, prev):
    global Count
    if len(Nums) == NumLen:
        if sum(Nums) == Num:
            Count += 1
        return
        
    for i in range(Length):
      #Use previous index to make combinations
        if Visited[i] != 1 and (len(Nums) == 0 or i > prev):
            Nums.append(NumList[i])
            Visited[i] = 1
            #Input previous index
            MakeNums(NumLen, i)
            Visited[i] = 0
            Nums.pop()
            
#Do it for every length possible
for i in range(1, Length+1):
    Visited = [0 for v in range(Length)]
    Nums = []
    MakeNums(i,-1)
    
print(Count)
