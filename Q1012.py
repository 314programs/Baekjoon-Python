#Set up inputs
import sys
input = sys.stdin.readline
casecount = int(input())
for g in range(casecount):
    x_Dimension, y_Dimension, CabbageNum = map(int, input().split())
    CabbageLocation = []
    for i in range(CabbageNum):
        CabbageLocation.append(list(map(int, input().split())))
        
#Set up directions
    Directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    Count = 0
#Finds nearby values using directions
    def Calculate(coord):
        CabbageLocation.pop(CabbageLocation.index(coord))
        for item in Directions:
            x = coord[0]+item[0]
            y = coord[1]+item[1]
#Repeat the function until it reached the boundary
            if [x,y] in CabbageLocation:
                Calculate([x,y])
        return
      
#Runs a loop to find groups using the Calculate function
    while len(CabbageLocation) != 0:
        for item in CabbageLocation:
            Calculate(item)
            Count += 1

    print(Count)
