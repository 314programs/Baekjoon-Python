#My dad had problems with this
#Maybe I should revise on maths
Num, divide_by, index = map(int, input().split())

if Num > divide_by:
    Num %= divide_by 
    Temp = 0
else:
    Temp = Num//divide_by
    Num %= divide_by 

for i in range(index):
    Num *= 10
    Temp = Num//divide_by
    Num %= divide_by 

print(Temp)
