import sys
input = sys.stdin.readline
TestCase = int(input())
for x in range(TestCase):
    x,y,m,n = map(int, input().split())

    def gcd(a,b):
        while b:
            a, b = b, a%b
        return a

    year = m

    TotalYear = (x*y)//gcd(x,y)

    while True:
        if year > TotalYear:
            print('-1')
            break
        temp = year % y
         
        if temp == 0:
            temp = y
            
        if temp == n:
            print(year)
            break
        year += x
 
 
