#Using shoelace formula
import math
Vertex_num = int(input())
Vertex_List = [list(map(int, input().split())) for v in range(Vertex_num)]
#Add the first element back
Vertex_List.append(Vertex_List[0])
Vertex_num += 1
#Seperate into 2 parts to avoid confusion
Total_Area_Add = 0
Total_Area_Subtract = 0

#Basic for loops for the formula
for i in range(Vertex_num-1):
    Total_Area_Add += Vertex_List[i][0] * Vertex_List[i+1][1]

for i in range(1, Vertex_num):
    Total_Area_Subtract += Vertex_List[i][0] * Vertex_List[i-1][1]
    
print('{:0.1f}'.format(round(0.5 * abs(Total_Area_Add - Total_Area_Subtract), 1)))
