#Take input
dimension, casecount = map(int, input().split())
rect_x, rect_y = dimension, dimension
CoordList = []

for i in range(casecount):
    x, y = map(int, input().split())
    CoordList.append([x,y])
    
for item in CoordList:
#Declare border
    if item[0] >= rect_x or item[1] >= rect_y or item[1] == 0 or item[0] == 0:
        continue
#Measure area
    if item[1]*rect_x > item[0]*rect_y:
        rect_y = item[1]
        
    else:
        rect_x = item[0]
    

print(rect_x*rect_y)
        
