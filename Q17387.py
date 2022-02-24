#https://jason9319.tistory.com/358
Line_1 = list(map(int, input().split()))
Line_2 = list(map(int, input().split()))

#A: Line1 0, 1
#B: Line1 2, 3
#C: Line2 0, 1
#D: Line2 2, 3

Intersection = False

def CCW(x1, y1, x2, y2, x3, y3):
    return ((x2-x1)*(y3-y1)) - ((y2-y1)*(x3-x1))

#CCW(C, D, A) * CCW(C, D, B)
Temp1 = CCW(Line_2[0], Line_2[1], Line_2[2], Line_2[3], Line_1[0], Line_1[1]) * CCW(Line_2[0], Line_2[1], Line_2[2], Line_2[3], Line_1[2], Line_1[3])
#CCW(A, B, C) * CCW(A, B, D)
Temp2 = CCW(Line_1[0], Line_1[1], Line_1[2], Line_1[3], Line_2[0], Line_2[1]) * CCW(Line_1[0], Line_1[1], Line_1[2], Line_1[3], Line_2[2], Line_2[3])


if Temp1 <= 0 and Temp2 <= 0:
    if Temp1 == 0 and Temp2 == 0:
        if (min(Line_2[0], Line_2[2]) <= Line_1[0] <= max(Line_2[0], Line_2[2]) and min(Line_2[1], Line_2[3]) <= Line_1[1] <= max(Line_2[1], Line_2[3])) or (min(Line_2[0], Line_2[2]) <= Line_1[2] <= max(Line_2[0], Line_2[2]) and min(Line_2[1], Line_2[3]) <= Line_1[3] <= max(Line_2[1], Line_2[3])): 
            Intersection = True
        elif (min(Line_1[0], Line_1[2]) <= Line_2[0] <= max(Line_1[0], Line_1[2]) and min(Line_1[1], Line_1[3]) <= Line_2[1] <= max(Line_1[1], Line_1[3])) or (min(Line_1[0], Line_1[2]) <= Line_2[2] <= max(Line_1[0], Line_1[2]) and min(Line_1[1], Line_1[3]) <= Line_2[3] <= max(Line_1[1], Line_1[3])): 
            Intersection = True
    else:
        Intersection = True
        

if Intersection: print(1)
else: print(0)
