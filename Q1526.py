Num = int(input())
for i in range(Num, -1, -1):
    if str(i).count('7') + str(i).count('4') == len(str(i)):
        print(i)
        break
