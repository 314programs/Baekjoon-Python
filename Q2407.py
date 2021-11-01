def Comb(top, bottom):
    return Fac(top)//(Fac(bottom)*Fac(top-bottom))

def Fac(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

N, M = map(int, input().split())
print(Comb(N, M))
