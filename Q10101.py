A = int(input())
B = int(input())
C = int(input())

if A+B+C == 180:
    if A == 60 and B == 60 and C == 60:
        print('Equilateral')
        
    elif len(set([A,B,C])) == 3:
        print('Scalene')
    else:
        print('Isosceles')
else:
    print('Error')
