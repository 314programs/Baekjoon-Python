Power = int(input())
#Fibonacci matrix
Matrix = [[1,1],[1,0]]

#Matrix multiplying
def Multiply(a, b):
    result = [[0 for v in range(2)] for v in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][k] += a[i][j] * b[j][k]
            #Divide the numbers constantly to prevent them from getting big
            result[i][j] %= (10**9) + 7
            
    return result

#Matrix powering
def power(p,m):
    if p == 1:
        return m
    
    else:
        if p%2 == 0:
            temp = power(p//2, m)
            return Multiply(temp, temp) 
        else:
            temp = power(p-1, m)
            return Multiply(temp, m)

result = power(Power, Matrix)

#Print
print(result[0][1])
