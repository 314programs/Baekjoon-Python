N = int(input())
#Make a list setups
CoordList = []
Result = []

UsedX = [0]*(N)
UsedGrad1 = [0]*(N+N-1)
UsedGrad1Negative = [0]*(N+N-1)

    
Count = 0

#BackTracking
def BackTrack(Y):
    if len(CoordList) == N:
        Result.append(1)
        return
    else:
#Only use x in a loop, don't use Y in a loop since same Y doesn't matter anyways
        for x in range(N):
            if UsedX[x] == 0 and UsedGrad1[x+Y] == 0 and UsedGrad1Negative[x-Y+N-1] == 0:
                CoordList.append([x,Y])
                UsedX[x] = 1
                UsedGrad1[x+Y] = 1
                UsedGrad1Negative[x-Y+N-1] = 1
                
                BackTrack(Y+1)
                
                UsedX[x] = 0
                UsedGrad1[x+Y] = 0
                UsedGrad1Negative[x-Y+N-1] = 0
                
                CoordList.pop()
BackTrack(0)
print(len(Result))
                    
    
