#I forgor how to format decimals...
Temp1 = float(input())
while True:
    Temp2 = float(input())
    if Temp2 == 999:
        break
    print("{:.2f}".format(Temp2-Temp1))
    Temp1 = Temp2
