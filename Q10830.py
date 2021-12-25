#Input
Dimension, Power = map(int, input().split())
Matrix = []

for i in range(Dimension):
    Matrix.append(list(map(int, input().split())))


def Multiply(a, b, n):
  #List for multiplication
    result = [[0 for v in range(Dimension)] for v in range(Dimension)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][k] += a[i][j] * b[j][k]
            #Divide to prevent values getting too big
            result[i][j] %= 1000
            
    return result
                
def power(d,p,m):
    if p == 1:
        return m
    
    else:
        if p%2 == 0:
          #Divide power by two if it is even
            temp = power(d, p//2, m)
            return Multiply(temp, temp, d) 
        else:
          #Subtract one from the power if its odd to make it even
            temp = power(d, p-1, m)
            return Multiply(temp, m, d)

result = power(Dimension, Power, Matrix)

#Print
for y in range(Dimension):
    for x in range(Dimension):
        print(result[y][x]%1000, end = " ")
    print()
