import math
Allow = 0.001
#Take input of the numbers inputed and save them as a float
x, y, c = map(float, input().split())

#Unknown distance will be between 0 and the smallest value of x and y
Minimum = 0
Maximum = min(x,y)

#Use coordinate geometry to calculate the c using the unknown distance
def Calculate(Center, X, Y, Height):
    H = (X**2 - Center**2)**0.5
    K = (Y**2 - Center**2)**0.5
    
    XCoord = H/((H+K)/Center)
    CalculatedC = XCoord*(K/Center)
    return CalculatedC - Height

#Use binary algorithm to find out the unknown distance quickly
while True:
    Middle = (Maximum+Minimum)/2
    CalculatedValue = Calculate(Middle, x, y, c)
    
    #If the calculated C if less than 10^-3, print the distance calculated and end the program
    if abs(CalculatedValue) < 0.001:
        print(str("%.3f" % round(Middle,3)))
        break

    if CalculatedValue > 0:
        Minimum = Middle
    else:
        Maximum = Middle
    
    

