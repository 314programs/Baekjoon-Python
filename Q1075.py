Number = input()
Divider = int(input())

for i in range(100):
    num = str(i)
    if len(str(i)) == 1:
        num = '0'+str(i)
    Cut = Number[:len(Number)-2]
    if int(Cut + num)%Divider == 0:
        print(num)
        break
